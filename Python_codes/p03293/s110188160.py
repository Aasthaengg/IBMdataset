s = str(input())
t = str(input())
n = len(s)
x = s
ans = 'No'
for _ in range(n):
    if x == t:
        ans = 'Yes'
        break
    nx = x[-1] + x[:n-1]
    x = nx
print(ans)