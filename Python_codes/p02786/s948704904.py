import bisect

H=int(input())
A=[2**x for x in range(51)]
index=bisect.bisect_right(A,H) 
print(sum(A[:index]))