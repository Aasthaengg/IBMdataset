n,x,t = map(int, input().split())
w = n//x
if (n % x) == 0:
    print(w * t)
else:
    w += 1
    print(w * t)