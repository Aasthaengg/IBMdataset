n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
p = []
ans = 0
x = sum(A)
k = 0
for i in range(n):
    if A[i] < B[i]:
        ans += 1
        k += A[i] - B[i]
    elif A[i] > B[i]:
        p.append(A[i] - B[i])
        
p.sort(reverse=True)
for i in p:
    if k >= 0:
        break
    k += i
    ans += 1

if k >= 0:
    print(ans)
else:
    print(-1)