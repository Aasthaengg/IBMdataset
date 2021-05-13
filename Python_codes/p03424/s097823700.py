n = int(input())
s = set(map(str, input().split()))

print("Three" if len(s) == 3 else "Four")