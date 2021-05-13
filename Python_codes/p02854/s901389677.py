n = int(input())
al = list(map(int, input().split()))
s = sum(al)

cnt = 0
i = 0
while cnt < s/2:
    cnt += al[i]
    i += 1

s1 = sum(al[0:i])-sum(al[i:])
s2 = sum(al[0:i-1]) - sum(al[i-1:])

if s1 < 0:
    s1 = -s1
if s2 < 0:
    s2 = -s2
print(min(s1, s2))