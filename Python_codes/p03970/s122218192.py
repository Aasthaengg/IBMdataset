def solve(s):
    return len(list(filter(lambda x: x[0] != x[1], zip(s, "CODEFESTIVAL2016"))))

print(solve(input()))