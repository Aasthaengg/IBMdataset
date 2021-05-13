A,B,C=map(int,input().split())
D=[]
for i in range(1,B+1):
    D.append((A*i)%B)
if C in D:
    print('YES')
else:
    print('NO')