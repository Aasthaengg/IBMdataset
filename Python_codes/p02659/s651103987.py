import sys
input = sys.stdin.readline

a,b = input().strip().split()
a = int(a)
b = b.replace('.','')
ans = (a*int(b))//100
print(ans)
