a, b, c  = map(lambda x: int(x),  input().split())
 
lis = [a, b, c]
lis.sort()

print(lis[0] + lis[1])