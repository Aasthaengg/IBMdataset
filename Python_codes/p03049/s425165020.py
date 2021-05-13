n = int(input())

kosu = [0,0,0]
ans = 0
for i in range(n):
    s = input()
    ans += s.count('AB')
    if s[0]=="B" and s[-1]=="A":
        kosu[2] += 1
        continue
    if s[0] == "B":
        kosu[1] += 1
    if s[-1] == "A":
        kosu[0] += 1

if kosu[2] == 0:
    ans += min(kosu[0],kosu[1])
else:
    if kosu[0]+kosu[1] >= 1:
        ans += min(kosu[0], kosu[1])+kosu[2]
    else:
        ans += kosu[2]-1

print(ans)