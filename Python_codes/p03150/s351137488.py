S = input()
k = 'keyence'
Srev = S[::-1]
krev = k[::-1]

ans = 'NO'
for i in range(8):
    if S[:i]==k[:i] and Srev[:(7-i)]==krev[:(7-i)]:
        ans = 'YES'

print(ans)