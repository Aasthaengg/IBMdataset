a = list(map(int,input().split()))
b = list(map(int,input().split()))

b.sort()
print(b[-1]-b[0])