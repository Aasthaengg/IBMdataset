a, b = list(map(int,input().split()))
tmp = a+b
if tmp%2==0:
    print(int(tmp/2))
else:
    print("IMPOSSIBLE")