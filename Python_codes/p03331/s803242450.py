N = int(input())
if N == 2:
    print(2)
    exit()
ans = float('inf')
for i in range(2,N):
    A = i
    B = N - i
    tmp = 0
    for k in str(A):
        tmp += int(k)
    for k in str(B):
        tmp += int(k)
    ans = min(ans,tmp)
print(ans)