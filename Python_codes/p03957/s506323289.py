def solve(s):
    key = "CF"
    position = 0
    for c in s:
        if key[position] == c:
            position += 1
            if position == len(key):
                return "Yes"
    return "No"

s = input()
print(solve(s))