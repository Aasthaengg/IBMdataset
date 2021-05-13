a,b,t = map(int,input().split())
count=0

for i in range(1,t+1):
    #print(i)
    if a*i<t+0.5:
        count+=b
print(count)
