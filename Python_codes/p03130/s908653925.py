l=[]
for i in range(3):
    l += list(map(int,input().split()))

for i in [1,2,3,4]:
    cnt=0
    for j in l:
        if i==j:
            cnt+=1
    if cnt==0 or cnt>2:
        print('NO')
        break
else:
    print('YES')