C = list(input() for i in range(2))
print("YES" if C[0]==C[1][::-1] else "NO")