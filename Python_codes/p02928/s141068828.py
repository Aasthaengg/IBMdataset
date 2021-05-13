N,K = map(int,input().split())
l = list(map(int,input().split()))

num1 = 0
num2 = 0

for i in range(N):
    for j in range(N):
        if i > j:
            if l[i] > l[j]:
                num2 += 1
        if j > i:
            if l[i] > l[j]:
                num1 += 1
                num2 += 1

print((num1 * K + num2 * (K*(K-1)//2)) % (10**9 + 7))