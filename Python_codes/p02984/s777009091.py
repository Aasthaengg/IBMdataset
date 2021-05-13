n = int(input())
a = list(map(int, input().split()))

target = sum(a)//2

b = a[1:n:2]
a.append(a[0])

ans = []
ans.append((target-sum(b))*2)

for i in range(n-1):
    num = a[i] - ans[i]//2
    ans.append(num*2)

for i in range(n):
    print(ans[i], end=' ')