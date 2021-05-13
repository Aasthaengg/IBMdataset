n = int(input())
l = []
pa = 0
pb = 0
pc = 0
for i in range(n):
    a,b,c = map(int,input().split())
    na = max((a+pb),(a+pc))
    nb = max((b+pa),(b+pc))
    nc = max((c+pa),(c+pb))
    pa = na
    pb = nb
    pc = nc

print(max(pa,pb,pc))