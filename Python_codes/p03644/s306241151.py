import sys

N = int(input())

if N == 1:
    print(1)
    sys.exit()

ans = 0
count_max = 0
for i in range(1, N+1):
    count = (i ^ (i-1)).bit_length() - 1
    if count_max < count:
        count_max = count
        ans = i

print(ans)