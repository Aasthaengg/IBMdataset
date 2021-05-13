K, T = map(int,input().split())
a = sorted(list(map(int,input().split())))
m = a[-1]
o = K-m
if m <= o:
    print(0)
else:
    print(m-o-1)
