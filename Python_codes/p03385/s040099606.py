S = input()
print("Yes" if all(c in S for c in "abc") else "No")