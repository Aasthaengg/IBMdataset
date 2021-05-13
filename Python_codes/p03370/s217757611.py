n,x = map(int,input().split())
m = [0]*n
for i in range(n):
    m[i] = int(input())
m = sorted(m)
x -= sum(m)
print(n+x//m[0])