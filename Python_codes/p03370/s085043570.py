n,x = map(int,input().split())
m = [int(input()) for _ in range(n)]
count = len(m)
x -= sum(m)
mn = min(m)
count += x//mn
print(count)