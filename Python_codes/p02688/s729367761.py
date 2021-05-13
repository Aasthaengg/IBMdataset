N, K = [int(i) for i in input().split(' ')]
s = [True] * N

for i in range(K):
    d = input()
    for j in input().split(' '):
        s[int(j) - 1] = False
print(len([i for i in s if i]))
