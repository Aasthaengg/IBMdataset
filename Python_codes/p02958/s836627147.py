N = int(input())
p = list(map(int,input().split()))
sort_p=sorted(p)
count = 0
for i,j in zip(p,sort_p):
    if(i!=j):
        count+=1
if(count==2 or count==0):
    print('YES')
else:
    print('NO')