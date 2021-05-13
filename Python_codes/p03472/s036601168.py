n,h = map(int,input().split())
a = []
b = []
for i in range(n):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
a.sort(reverse=True)
b.sort(reverse=True)
ans = 0
damage = 0
for i in b:
    if i > a[0]:
        damage += i
        ans += 1
        if damage >= h:
            print(ans)
            exit()
h -= damage
print(ans + (h+a[0]-1)//a[0])