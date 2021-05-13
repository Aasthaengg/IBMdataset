from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A = [min(8, a // 400) for a in A]
CA = Counter(A)
num = 0
for i in range(8):
    if CA[i]:
        num += 1

num_8 = CA[8]
saidai = num + num_8

saisho = max(1, num)
print(saisho, saidai)

