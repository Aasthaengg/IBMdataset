N = int(input())
count = 0

while N > 1:
    N = int(N/2)
    count += 1
print(2**count)