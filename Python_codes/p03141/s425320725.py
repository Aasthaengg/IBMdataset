n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

s = [(a+b, a, b) for a, b  in ab]
s.sort(reverse = True)
# print(s)

t = 0
a = 0
for i in range(n):
    if i % 2 == 0:
        t += s[i][1]
    else:
        a += s[i][2]

print(t-a)