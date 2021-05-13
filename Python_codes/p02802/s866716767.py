n,m=map(int,input().split())

if m==0:
    print(0,0)
    import sys
    sys.exit()

p=[list(input().split()) for _ in range(m)]
correct=set([p[i][0] for i in range(m) if p[i][1]=='AC'])

sum_wa=0
data=[0]*n

for i in range(m):
    if p[i][0] in correct and data[int(p[i][0])-1]==0:
        if p[i][1]=='WA':
            sum_wa+=1
        else:
            data[int(p[i][0])-1]=1

print(sum(data),sum_wa)