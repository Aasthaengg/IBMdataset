N = int(input())
K = int(input())
num = 1
for i in range(N):
    if num > K:
        num += K
    else:
        num = num*2
print(num)