j=[]
while True:
    a,b=map(int,input().split())
    if a==b==0:break
    j.append(sorted([a,b]))

for i in range(len(j)):
    print('{0[0]} {0[1]}'.format(j[i]))
