h, a = map(int, input().split())
arr = list(map(int, input().split()))
for i in arr:
    h-=i
print("Yes" if h<=0 else "No")