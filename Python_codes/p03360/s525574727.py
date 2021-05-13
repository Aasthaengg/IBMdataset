a,b,c = map(int,input().split())
k = int(input())
tmp = a + b + c - max(a,b,c)
print(tmp+max(a,b,c)*(2**k))