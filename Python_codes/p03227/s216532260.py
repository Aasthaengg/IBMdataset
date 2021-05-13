S = input()
print(S if len(S) == 2 else ''.join(reversed(list(S))))