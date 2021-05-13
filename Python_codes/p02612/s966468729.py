N = int(input())
a,b = divmod(N,1000)
print((b,1000-b)[b != 0])