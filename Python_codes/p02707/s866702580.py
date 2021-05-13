N = int(input())
A = list(map(int, input().split()))
person = [0] * N
for i in range(0, N - 1):
    person[A[i] - 1] += 1
for count in person:
    print(count)
