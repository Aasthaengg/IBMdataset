n,x = map(int,input().split())
m = list(int(input()) for i in range(n))

print((x - sum(m)) // min(m) + n)
