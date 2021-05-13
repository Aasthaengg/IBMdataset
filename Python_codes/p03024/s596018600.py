line = list(input())
win = line.count("o")
match = 15-len(line)
if win + match > 7:
    print("YES")
else:
    print("NO")
