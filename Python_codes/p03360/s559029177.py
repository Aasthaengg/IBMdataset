a,b,c = map(int,input().split())
k = int(input())
s = sum([a,b,c])
m = max([a,b,c])
s += m*(2**k-1)
print(s)