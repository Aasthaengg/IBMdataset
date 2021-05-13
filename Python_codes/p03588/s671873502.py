n = int(input())
x = []
for i in range(n):
    y = list(map(int,input().split()))
    x.append(y)

x.sort(reverse=True)
ans = x[0][0] + x[0][1]
print(ans)