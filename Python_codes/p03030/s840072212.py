n = int(input())
chk = []
for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    chk.append([s, -p])
s = sorted(chk)
#print(s)
#print(chk)
for i in s:
    print(chk.index(i)+1)