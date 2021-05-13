n = int(input())
a = [int(input()) for _ in range(5)]

m = min(a)

t = (n-1) // m

print(t+5)
