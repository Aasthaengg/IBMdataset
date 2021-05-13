import sys
n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()
y = lambda x : x%10
mx = sum(ls)
new = list(map(y,ls))
if sum(new) == 0:
    print(0)
    sys.exit()
if mx%10 != 0:
    print(mx)
else:
    for i in range(n):
        nx = mx - ls[i]
        if nx%10 != 0:
            print(nx)
            sys.exit()