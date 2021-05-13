n = int(input())
vl = list(map(int, input().split()))
vl.sort()

ans = (vl[0]+vl[1])/2
if len(vl) == 2:
    print(ans)
    exit()

for v in vl[2:]:
    ans = (ans + v)/2

print(ans)