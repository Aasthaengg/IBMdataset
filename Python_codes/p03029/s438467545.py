A,P = map(int,input().split())

pie = (3*A + P) / 2
if pie*2 % 2 == 0:
    print(int(pie))
elif pie*2 % 2 == 1:
    print(int(pie - 0.5))