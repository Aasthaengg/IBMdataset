import bisect
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
A_cum = [0]
B_cum = [0]
A_cum[0] = A[0]
for j in range(len(A)-1):
    A_cum.append(A_cum[j]+ A[j+1])
B_cum[0] = B[0]
for l in range(len(B)-1):
    B_cum.append(B_cum[l] + B[l+1])
for i in range(len(A_cum)):
    k = A_cum[i]
    if k >K:
        break
    b = bisect.bisect(B_cum,K-k)
    check = i+b+1
    if check>ans:
        ans = check
check = bisect.bisect(B_cum,K)
if check>ans:
    ans = check    
print(ans)