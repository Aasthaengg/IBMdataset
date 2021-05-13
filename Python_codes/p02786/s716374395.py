H = int(input())
L = len(bin(H)) - 2
ans = 0
for j in range(L):
    ans += 2 ** j
print(ans)
