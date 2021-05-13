import sys
A,B,C = map(int,input().split())

for i in range(1,B+1):
    tmp = i * A
    if tmp%B==C:
        print('YES')
        sys.exit()
print('NO')
