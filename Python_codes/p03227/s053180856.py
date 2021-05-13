S = [i for i in input()]
if len(S)==2:
    print("".join(S))
else:
    print("".join(S[::-1]))