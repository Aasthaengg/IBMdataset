data = list(map(int, input().split()))
A = data[0]
B = data[1]
C = data[2]

rest = A - B
remain = max(0, C - rest)

print(remain)
