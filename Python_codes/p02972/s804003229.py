N = int(input())
a = [0] + list(map(int,input().split()))
ans = [0]*(N+1)
for k in range(N,0,-1):
    temp = 0
    l = k
    while l <= N:
        temp += ans[l]
        l += k
    if a[k] == 1 and temp%2 == 0:
        ans[k] = 1
    elif a[k] == 0 and temp%2 == 1:
        ans[k] = 1
b = []
for k in range(1,N+1):
    if ans[k] == 1:
        b.append(k)
print(len(b))
print(*b)
