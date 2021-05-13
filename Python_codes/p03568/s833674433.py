N = int(input())
A = list(map(int, input().split()))

all_num = 3 ** N
even = 1

for a in A:
    if a % 2 == 0:
        even *= 2

print(all_num - even)