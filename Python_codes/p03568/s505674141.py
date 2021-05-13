N = int(input())
A = [int(x) for x in input().split()]

odd = 0
for a in A:
    if a%2==0:
        odd += 1

print(3**N - 2**odd)
