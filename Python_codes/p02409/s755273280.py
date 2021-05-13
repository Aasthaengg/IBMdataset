n = int(input())
values = [input().split() for i in range(n)]

# Initialize Array
a = [["#" if i > 0 and i % 4 == 3 else 0 for j in range(10)] for i in range(15)]

# Search
for value in values:
    b, f, r, v = map(int, value)
    a[4 * b + f - 5][r - 1] += v

# Output
for i in range(15):
    row_output = ""
    for j in range(10):
        if i > 0 and i % 4 == 3:
            row_output += "##"
        else:
            row_output += " " + str(a[i][j])
    print(row_output)

