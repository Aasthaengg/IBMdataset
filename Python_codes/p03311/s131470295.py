n = int(input())
s = [int(x) for x in input().split()]

for i in range(n):
    s[i] = s[i] - i - 1

s.sort()
a = s[(n+1)//2 - 1]

res = 0
for ss in s:
    res += abs(ss - a)
print(res)
