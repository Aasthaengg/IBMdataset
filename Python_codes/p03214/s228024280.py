n = int(input())
a = [int(i) for i in input().split()]
mean = sum(a) / n
a = [abs(i - mean) for i in a]
print(a.index(min(a)))