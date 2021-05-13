C1 = input()
C2 = input()

ans = 'YES'
for i in range(1, len(C1)+1):
    if C1[i-1] != C2[-i]:
        ans = 'NO'

print(ans)