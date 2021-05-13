import sys
A,B,C=map(int,input().split())

for i in range(10**6):
    if A*i%B==C:
        print('YES')
        sys.exit()
    else:
        continue
print('NO')