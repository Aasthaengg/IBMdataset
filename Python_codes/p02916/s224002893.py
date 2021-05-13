N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total = sum(B)
memo = 20
for i in A:
    if memo+1 == i:
        total += C[i-2]
    memo = i

print(total)
