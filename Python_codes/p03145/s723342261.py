a,b,c = map(int, input().split())
print(int(a * b * c / max(a,b,c) / 2))