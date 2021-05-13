S = list(input())
k = len(S)
if S.count("o") + (15 - k) >= 8:
    print("YES")
else:
    print("NO")
