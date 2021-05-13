N = input()

S = sum(int(d) for d in N)

print("Yes" if S % 9 == 0 else "No")