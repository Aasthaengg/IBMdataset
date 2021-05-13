s = "".join(sorted(list(input())))
t = "".join(sorted(list(input()), reverse=True))

print("Yes") if t > s else print("No")
