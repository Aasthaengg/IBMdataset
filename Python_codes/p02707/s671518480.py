N = int(input())
A = [int(i) for i in input().split(' ')]
subords = [0] * N
for a in A:
    subords[a - 1] += 1

print('\n'.join([str(i) for i in subords]))
