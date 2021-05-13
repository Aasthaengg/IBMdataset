A,V = map(int,input().split())
B,W = map(int, input().split())
T = int(input())
if A<B and V*T+A>=W*T+B:
    print('YES')
elif A>B and A-T*V<=B-T*W:
    print('YES')
else:
    print('NO')