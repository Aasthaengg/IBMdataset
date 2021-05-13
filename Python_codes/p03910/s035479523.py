n = int(input())
ans = []
a = 0
for i in range(1,n+1):
    a += i
    ans.append(i)
    if a >= n:
        break
a -= n
for x in ans:
    if x != a:
        print(x)