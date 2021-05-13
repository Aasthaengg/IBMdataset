A = []
for i in range(5):
    A.append(int(input()))
K = int(input())

print(':(' if A[4]-A[0] > K else 'Yay!')