l=[0]*120
s="#"*20
n=input()
while n:n-=1;b,f,r,v=map(int,raw_input().split());l[b*30+f*10+r-41]+=v
print"",
while 1:
 n+=1;print l[n-1],
 if n==120:break
 if n%30==0:print;print s,
 if n%10==0:print;print"",