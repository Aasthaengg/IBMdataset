S = input()

print(len([0 for index, c in enumerate(S[1:], 1) if c != S[index - 1]]))
