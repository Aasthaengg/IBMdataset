a,b=map(int,input().split())
c=[]
for _ in range(a):
    c.append(list(map(int,input().split())))
result=[]
for i in range(a):
    if c[i][1]<=b:
        result.append(c[i][0])
if result==[]:
    print('TLE')
    exit()
print(min(result))