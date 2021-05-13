# input
numbers = list(map(int, input().split()))
K = int(input())

# check
for c in range(K):
    max_num = max(numbers)
    max_idx = numbers.index(max_num)
    numbers[max_idx] *= 2

print(sum(numbers))