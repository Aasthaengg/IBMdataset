S = input().strip()
k = len(S)
n = S.count("o")
if n+15-k>=8:
    print("YES")
else:
    print("NO")