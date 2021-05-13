N = input()

print("Yes" if N == "".join(reversed(list(N))) else "No")
