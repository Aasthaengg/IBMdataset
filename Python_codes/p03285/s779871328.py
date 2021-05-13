# B - Cakes and Donuts

N = int(input())

ans = 'No'
for i in range(26):
    for j in range(16):
        if 4*i+7*j == N:
            ans = 'Yes'
            break
    else:
        continue
    break
print(ans)