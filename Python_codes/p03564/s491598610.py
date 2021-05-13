N = int(input())
K = int(input())
num = 1
for x in range(N):
    if num * 2 < num + K:
        num *= 2
    else:
        num += K
print(num)
