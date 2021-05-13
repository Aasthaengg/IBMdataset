s = list(input())

print("".join([s[0]] + [str(len(s[1:-1]))] + [s[-1]]))