N = int(input())
A = list(map(int, input().split()))

num = 1
odd = 1

for a in A:
    num *= 3
    if a % 2 == 0:
        odd *= 2

print(num - odd)
