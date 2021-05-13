while 1:
 n=int(input())
 if n==0:break
 s=input().split()
 a=sum([int(x) for x in s])/n
 print((sum([int(x)**2 for x in s])/n-a*a)**.5)