n, i = map(int, input().split())
print(n-i+1 if abs(n - i ) >= n//2 else n - i + 1)