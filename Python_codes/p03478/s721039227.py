n,a,b=map(int,input().split())
list=[]
for i in range(0,n+1):
    s1=int(i%10)
    s2=int((i-s1)%100/10)
    s3=int((i-s1-10*s2)%1000/100)
    s4=int((i-s1-10*s2-100*s3)%10000/1000)
    s5=int((i-s1-10*s2-100*s3-1000*s4)%100000/10000)
    if s1+s2+s3+s4+s5>=a and s1+s2+s3+s4+s5<=b:
        list.append(i)
print(sum(list))