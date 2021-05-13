A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())


if V<=W:
    print('NO')
else:
    if abs(A-B)/(V-W)<=T:
        print('YES')
    else:
        print('NO')