import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

res = b
res += min(c,a+b+1)
print(res)