S = input()
l0 = S.count("0")
l1 = len(S) - l0

print(2 * min([l0, l1]))