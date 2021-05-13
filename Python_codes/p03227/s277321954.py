seq = input()
if len(seq) == 2:
    print(seq)
else:
    print("".join(list(seq)[::-1]))