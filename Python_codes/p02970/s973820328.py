n,d = map(int, input().split())

t = n//(2*d+1)
if n > t*(2*d+1):
    print(t+1)
else:
    print(t)