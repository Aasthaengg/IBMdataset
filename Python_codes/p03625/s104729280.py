n = int(input())
A = sorted(list(map(int, input().split())), reverse = True)
l = 0
ln = []
for a in A:
    if l == a:
        ln.append(a)
        l = 0
    else:
        l = a
    if len(ln) == 2:
        break
if len(ln) == 2:
    print(ln[0]*ln[1])
else:
    print(0)