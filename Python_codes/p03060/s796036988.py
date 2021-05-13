n = int(input())
a = [i - j for i, j in zip([int(i) for i in input().split()], [int(i) for i in input().split()])]
print(sum(filter(lambda c: c > 0, a)))