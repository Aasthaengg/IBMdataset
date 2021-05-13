N = int(input())
K = int(input())
num = 1
for i in range(N):
    if num >= K:
        num += K
    elif num < K:
        num += num
print(num)