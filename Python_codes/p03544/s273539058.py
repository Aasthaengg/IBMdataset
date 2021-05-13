N = int(input())
L = [0] * 90
L[0] = 2
L[1] = 1
for i in range(2, len(L)):
    L[i] = L[i - 1] + L[i - 2]
# print(f'{L=}')
ans = L[N]
print(ans)
