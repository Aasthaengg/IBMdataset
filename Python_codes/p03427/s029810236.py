N = input()
if N[0] == "9":
    if N[1:] == "9" * len(N[1:]):
        print(9 * len(N))
    else:
        print(9 * len(N) - 1)
else:
    if N[1:] == "9" * len(N[1:]):
        print(int(N[0]) + 9 * len(N[1:]))
    else:
        print(int(N[0]) + 9 * len(N[1:]) - 1)

