from collections import Counter

n = int(input())
al = [int(input()) for _ in range(n)]
al_s = sorted(al, reverse=True)
c = Counter(al_s)
ck = list(c.keys())
cv = list(c.values())


for a in al:
    if a == ck[0]:
        if cv[0] == 1:
            print(ck[1])
        else:
            print(ck[0])
    else:
        print(ck[0])

