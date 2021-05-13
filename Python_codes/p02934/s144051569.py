N = int(input())
A = list(map(int, input().split()))

denominator = 0

for a in A:
    denominator += 1/a

answer = 1/denominator

print(answer)
