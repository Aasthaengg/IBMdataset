a = input("").split(" ")
a = [int(aa) for aa in a]
b = input("").split(" ")
b = [int(bb) for bb in b]
Al = []
N = a[0]
C = a[2]
ans = 0
for aaa in range(N):
    al = input("").split(" ")
    al = [int(aal) for aal in al]
    Al.append(al)
for c in Al:
    n = 0
    i = 0
    for d in c:
        n += d*b[i]
        i += 1
    if n+C > 0:
        ans += 1
print(ans)