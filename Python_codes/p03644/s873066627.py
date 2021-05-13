N = int(input())

L = [0] * 101
for i in range(1, 101):
    cnt = 0
    tmp = i
    while tmp % 2 == 0:
        cnt += 1
        tmp //= 2
    L[i] = cnt

print(L.index(max(L[1:N+1])) if N !=1 else 1)