N = input()
reversed_N = "".join([str(x) for x in N[::-1]])

if N == reversed_N:
    print("Yes")
else:
    print("No")
