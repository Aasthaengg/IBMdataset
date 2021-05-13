a,b,c = map(int, input().split())
print(max(a,b,c)*10 - max(a,b,c) + sum([a,b,c]))