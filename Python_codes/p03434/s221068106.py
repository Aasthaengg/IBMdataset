N = int(input())
A = [int(x) for x in input().split()]

A.sort(reverse = True)

alc = 0
bob = 0

N -= 1
end = int(N/2) + 1

if N % 2 == 0:
    f = 1
else:
    f = 0

for i in range(0, end):
    alc += A[2*i]
    if f == 1 and 2*i == N:
        break
    bob += A[2*i+1]

print(alc-bob)