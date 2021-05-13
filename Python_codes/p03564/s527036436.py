N = int(input())
K = input()
num = 1
ops = ["*2", "+" + K]

for _ in range(N):
    min = -1
    for op in ops:
        result = eval(str(num) + op)
        if min == -1 or result < min:
            min = result
    num = min

print(num)