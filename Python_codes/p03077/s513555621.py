N = int(input())
T = []
for i in range(5):
    T.append(int(input()))
k = 0
for i in range(5):
    if N % T[i] == 0:
        k = max(k, N//T[i])
    else:
        k = max(k, N//T[i] + 1)
print(4 + k)