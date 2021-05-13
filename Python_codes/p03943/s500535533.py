li = list(map(int, input().split()))
li = sorted(li)
print("Yes" if li[0]+li[1]==li[2] else "No")