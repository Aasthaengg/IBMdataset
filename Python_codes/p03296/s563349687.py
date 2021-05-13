N = int(input())
A = list(map(int, input().split()))

cont = []
c = 1
for i in range(N-1):
    if A[i] == A[i+1]:
        c += 1
    else:
        cont.append(c)
        c = 1
else:
    cont.append(c)

# print(cont)
ans = 0
for ci in cont:
    ans += ci // 2
print(ans)