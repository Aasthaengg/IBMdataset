N = input()
if len({c for c in N[:3]}) == 1 or len({c for c in N[1:]}) == 1:
    print("Yes")
else:
    print("No")
