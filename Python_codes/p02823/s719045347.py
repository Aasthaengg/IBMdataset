n, a, b = map(int, input().split())
print([(b-a)//2, min(a-1, n-b) + 1 + (b-a-1)//2][a%2-b%2])