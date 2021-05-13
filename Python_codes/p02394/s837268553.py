hoge = list(map(int, input().split()))
W=hoge[0]
H=hoge[1]
x=hoge[2]
y=hoge[3]
r=hoge[4]

if 0<=x-r and x+r<=W and 0<=y-r and y+r<=H:
    print("Yes")
else:
    print("No")

