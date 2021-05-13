import sys
S = "".join(sorted(input()))
T = "".join(sorted("".join(sorted(input())), reverse=True))
print("Yes" if S < T else "No")