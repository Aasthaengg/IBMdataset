import collections

n = int(input())
an = []
for i in range(n):
    a = input()
    an.append(a)

c = list(collections.Counter(an).values())
Ans = 0
for i in range(len(c)):
    if int(c[i]) % 2 == 1:
        Ans = Ans + 1

print(Ans)