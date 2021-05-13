S = input().split("hi")
S = filter(lambda x: x != "", S)
print("Yes" if not tuple(S) else "No")