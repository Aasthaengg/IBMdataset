A, B, T = map(int, input().split())
num = A
count = 0
while num <= T:
    count += B
    num += A
print(count)
