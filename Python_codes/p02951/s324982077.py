a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)
if (C - (A - B)) < 0:
    print(0)
else:
    print(C - (A - B))