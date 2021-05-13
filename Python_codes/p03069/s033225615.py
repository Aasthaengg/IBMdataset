from sys import stdin
n = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
kuro = s.count("#")
shiro = n-kuro
mi = shiro
k = 0
sh = shiro
for i in range(n):
    if s[i] == "#":
        k += 1
    else:
        sh -= 1
    mi = min(mi,k+sh)
print(mi)