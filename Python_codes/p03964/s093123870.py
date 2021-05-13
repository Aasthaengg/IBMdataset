N = int(input())
ansT = 1
ansA = 1
for i in range(N):
    T, A = map(int,input().split())
    if int(ansT / T) > int(ansA / A):
        ansT = T * int((ansT + T - 1) // T)
        ansA = A * int((ansT + T - 1) // T)
    else:
        ansT = T * int((ansA + A - 1) // A)
        ansA = A * int((ansA + A - 1) // A)

print(int(ansT + ansA))
