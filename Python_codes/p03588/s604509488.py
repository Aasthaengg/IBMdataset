def LI():
    return list(map(int, input().split()))


N = int(input())
ansA = 0
ansB = 0

for _ in range(N):
    A, B = LI()
    if ansA > A:
        continue
    ansA = A
    ansB = B
print(ansA+ansB)
