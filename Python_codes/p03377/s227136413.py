
A, B, X = map(int, input().split())

print("YES" if (X-A)>=0 and (A+B-X)>=0 else "NO")