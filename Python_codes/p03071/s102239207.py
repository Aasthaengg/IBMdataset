A, B = map(int, input().split(' '))

large = max(A, B)
small = min(A, B)

total = large
large -= 1
total += max(large, small)

print(total)
