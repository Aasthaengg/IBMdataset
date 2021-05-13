n = int(input())
k = int(input())
x = int(input())
y = int(input())

ans = []
if n>k:
    for i in range(k):
        ans.append(x)

    for i in range(n-k):
        ans.append(y)
else:
    for i in range(n):
        ans.append(x)
print(sum(ans))
