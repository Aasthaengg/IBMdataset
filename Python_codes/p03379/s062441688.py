import copy
N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

first_harf = Y[:int(N/2)]
second_harf = Y[int(N/2):]

for i in range(N):
    if X[i] <= first_harf[-1]:
        print(second_harf[0])
    else:
        print(first_harf[-1])
