S = input()

words = []
for s in S:
    if s not in words:
        words.append(s)
    else:
        print("no")
        break
else:
    print("yes")