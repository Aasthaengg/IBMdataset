S = list(input())
K, L = len(S), S.count("x")
print("YES" if -L + 15 >= 8 else "NO")