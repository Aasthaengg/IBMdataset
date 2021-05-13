n = int(input())
l = list(map(int,input().split()))
sl = sorted(l)

print(['No','Yes'][sl[-1]<sum(sl[:-1])])