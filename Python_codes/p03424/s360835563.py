n=int(input())
s=list(map(str,input().split()))
print("Three" if len(set(s))==3 else "Four")