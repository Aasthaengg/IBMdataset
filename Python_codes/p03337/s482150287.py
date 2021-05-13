a,b = map(int,input().split())
A = [a+b,a-b,a*b]
A.sort()
print(A[-1])