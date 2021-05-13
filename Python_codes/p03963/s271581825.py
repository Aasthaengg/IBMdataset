_input = list(map(int, input().split(" ")))
n = _input[0]
k = _input[1]

result = k * (k - 1) ** (n - 1)

print(result)