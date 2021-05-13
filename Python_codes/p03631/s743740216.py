n = list(input())
print("Yes" if n[:2]==n[1:][::-1] else "No")