n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
m = 0
for i in range(n-1):
    s = sum(a1[:i+1]) + sum(a2[i:])
    m = max(m,s)
if n == 1:
    m = sum(a1) + sum(a2)
print(m)