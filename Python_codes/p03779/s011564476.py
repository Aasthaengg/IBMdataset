import bisect
x = int(input())
A = [n*(n+1)//2 for n in range(10**5)]
 
print(bisect.bisect_left(A,x))