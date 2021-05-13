S = "".join(sorted(list(input())))
T = "".join(sorted(list(input()), reverse=True))
print("Yes") if S < T else print("No")
