n, l = map(int, input().split())
sumn = []
ans = 0
for i in range(n):
    t = l + i
    sumn.append(t)
sumn = sorted(sumn, key=lambda x: abs(x))
print(sum(sumn[1:]))