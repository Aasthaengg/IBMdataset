a, b = map(int, input().split())

if a == b:
    operator = "=="
else:
    operator = ">" if a > b else "<"
print("a {0} b".format(operator))