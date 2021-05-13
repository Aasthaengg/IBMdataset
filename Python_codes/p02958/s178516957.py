n = int(input())
p = [int(s) for s in input().split()]
sortedP = sorted(p)
sortedP.sort(key=int)
diffcount = 0
for i in range(n):
    if p[i] != sortedP[i]:
        diffcount += 1
if diffcount == 0 or diffcount == 2:
    print("YES")
else:
    print("NO")