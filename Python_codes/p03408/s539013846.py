n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
maxi = 0
for i in s:
    cnt = s.count(i) - t.count(i)
    maxi = max(maxi,cnt)
print(maxi)