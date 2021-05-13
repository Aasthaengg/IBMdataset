n = int(input())

t = [int(input()) for _ in range(5)]

q, r = divmod(n, min(t))

if r > 0:
    q += 1
    
print(q+4)