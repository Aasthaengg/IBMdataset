N = int(input())
K = int(input())
num = 1
for n in range(N):
    A = num * 2
    B = num + K
    if A > B:
        num = B
    else:
        num = A
print(num)