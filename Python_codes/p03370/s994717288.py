n, x = list(map(int, input().split()))
m = [int(input()) for _ in range(n)]
cake = len(m)
s = min(m)
print(cake + (x - sum(m)) // s)
