n=int(input())
s=list(input().split())
print("Three" if len(set(s))==3 else "Four")