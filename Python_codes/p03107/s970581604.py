S = input()
zero = S.count("0")
one = len(S) - zero

print(min(zero, one)*2)