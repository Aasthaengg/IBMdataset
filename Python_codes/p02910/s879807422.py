S = input()
print("Yes" if all(s in ["R","U","D"] for s in S[::2]) \
      and all(s in ["L","U","D"] for s in S[1::2]) else "No")