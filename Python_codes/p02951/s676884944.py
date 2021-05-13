
[A,B,C] = list(map(int,input().split()))

out = C - (A-B)

if out>=0:
    print(out)
else:
    print(0)