import fileinput

for line in fileinput.input():
    tokens = list(map(int, line.strip().split()))
    a, b, c = tokens[0], tokens[1], tokens[2]

    if a < b and b < c:
        print("Yes")
    else:
        print("No")