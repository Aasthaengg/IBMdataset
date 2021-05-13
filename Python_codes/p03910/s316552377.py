n = int(input())
cou = 0
p = set()
for i in range(n):
    cou += i+1
    p.add(i+1)
    if cou == n:
        break
    elif cou > n:
        p = p - {cou-n}
        break

for i in p:
    print(i)