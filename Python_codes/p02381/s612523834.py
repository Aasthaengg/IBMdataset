while 1:
 n=int(input())
 if n==0:break
 s=list(map(int,input().split()))
 a=sum(s)/n
 print((sum([x*x for x in s])/n-a*a)**.5)
