n,x = list(map(int,input().split()))
m = [int(input()) for _ in range(n)]
count = 0
m.sort()
x -= sum(m)
print(n + x // m[0])
