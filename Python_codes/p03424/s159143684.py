n = int(input())
s = list(set(list(input().split())))
print("Three" if len(s)==3 else "Four")