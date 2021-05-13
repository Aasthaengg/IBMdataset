N = int(input())
A = [int(x) for x in input().split()]
ki_count = 0
for a in A:
    if a % 2 == 1:
        ki_count += 1
print(3**N - 2**(N-ki_count))
