S = input()
if len(set(S[::2]) - {"R","U","D"}) == 0 and len(set(S[1::2]) - {"L","U","D"}) == 0:
    print("Yes")
else:
    print("No")