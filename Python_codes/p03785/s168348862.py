n,c,k=map(int,input().split())
t=[0]*n
for i in range(n):
    t[i]=int(input())
t.sort()
s=0
lt=0
ln=0

if c==1:
    print(n)
    exit()
for i in range(n):

    if i==0:
       lt=i
       ln+=1

    else:
        if t[i]-t[lt]>k:
            s+=1
            lt=i
            ln=0

        ln+=1
        if ln==c:
            s+=1
            lt=i+1
            ln=0

        #print(i, s, lt, ln)


    
if ln>0:
    s+=1

print(s)
