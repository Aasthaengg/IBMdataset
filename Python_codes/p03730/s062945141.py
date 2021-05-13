a,b,c=map(int,input().split())
x=0
for i in range(b):
    x+=a
    if x%b==c:
        print('YES')
        x='-1'
        break
if x!='-1':
    print('NO')