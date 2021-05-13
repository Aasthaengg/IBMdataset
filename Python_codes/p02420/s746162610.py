while 1:
    lines = input()
    if lines == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        lines = lines[h:] + lines[:h]
    print(lines)