n, p = map(int, input().split())
A = list(map(int, input().split()))
even = 0
odd = 0

for i in range(n):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1

even_answer = 2 ** even

check = p


def kaijo(i):
    if (i == 1) or (i == 0):
        return 1
    return i * kaijo(i - 1)


odd_answer = 0
while check <= odd:
    # print(kaijo(n) / kaijo(check) / kaijo(n - check))
    odd_answer = odd_answer + (kaijo(odd) / kaijo(check) / kaijo(odd - check))
    # print(odd_answer)
    check += 2

print(int(odd_answer * even_answer))
