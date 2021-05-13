N = int(input())
A = list(map(int,input().split()))

li = [0 for i in range(N)]
ans = 1

for i in range(N):
    a = A[i]
    if a>0:
        ans *= min(3-li[a],li[a-1]-li[a])
        ans %= 10**9+7
        li[a] += 1
    elif a==0:
        ans *= 3-li[0]
        li[a] += 1
    # print(i,ans)

print(ans)