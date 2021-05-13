S = input()
left = 15 - len(S)
now = sum([1 for s in S if s == "o"])
if now + left >= 8:
    print("YES")
else:
    print("NO")
