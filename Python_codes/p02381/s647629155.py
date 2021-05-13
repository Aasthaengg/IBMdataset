while 1:
 n=int(input())
 if n==0:break
 s=[int(x) for x in input().split()]
 print((sum([(m-sum(s)/n)**2 for m in s])/n)**.5)