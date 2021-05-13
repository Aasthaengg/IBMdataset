N,M = map(int,input().split())

a = 2**M

b= M*1900+(100*(N-M))
print(a*b)