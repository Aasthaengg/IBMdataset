N = int(input())
A = list(map(int, input().split()))
Q = int(input())

heavy = [0] * (10 ** 5 + 1)
for x in A:
    heavy[x] += 1
suma = sum(A)

for i in range(Q):
    B, C = map(int, input().split())
    suma -= B * heavy[B]
    suma += C * heavy[B]
    heavy[C] += heavy[B]
    heavy[B] = 0
    print(suma)
