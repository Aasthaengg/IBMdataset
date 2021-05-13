k,t = map(int,input().split())
a = sorted(list(map(int,input().split())))[::-1]
a1 = a[0]
a2 = sum(a[1:])
if a1-1<=a2:
    print(0)
else:
    print(a1-1-a2)