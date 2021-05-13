import sys
A,B,C = map(int,input().split())
#ln = 100//A+1
for i in range(1,100):
    if (A*i-C)% B == 0:
        print('YES')
        sys.exit()
print('NO')