N = int(input())
A = list(map(int, input().split()))
A.append(0)

kabu = 0
en = 1000

for i in range(N):
    a, b = divmod(en, A[i])
    kabu += a
    en = b
    if A[i+1] < A[i]:
        en += kabu*A[i]
        kabu = 0

print(en)