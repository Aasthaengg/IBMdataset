S, c = list(map(int, input().split()))
chalf = c//2
b = 0
if S < chalf:
    b = chalf - -(-(S+chalf)//2)
    print(int(S+b))
elif c < 2:
    print(0)
else:
    print(min(S,chalf))
