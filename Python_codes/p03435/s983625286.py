import sys
input = sys.stdin.readline

c11,c12,c13 = list(map(int,input().split()))
c21,c22,c23 = list(map(int,input().split()))
c31,c32,c33 = list(map(int,input().split()))

for a1 in range(0,101):
    b1 = c11-a1
    b2 = c12-a1
    b3 = c13-a1
    a2 = c21-b1
    a3 = c31-b1
    if a2+b2 == c22 and a3+b2 == c32 and a2+b3 == c23 and a3+b3 == c33:
        print('Yes')
        exit()

print('No')
