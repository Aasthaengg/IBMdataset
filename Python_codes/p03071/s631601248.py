a,b = map(int, input().split())
l = [a+a-1, a+b, b+b-1]
print(max(l))