#C - One Quadrillion and One Dalmatians
N = int(input())
A = []
for i in range(1,20):
    a = N%26
    if a == 0:
        N -= 26
        A.append(26)
    else:
        N -= a
        A.append(a)
    if N<=0:
        break
    N //= 26
ans = [chr(j-1+ord('a')) for j in A]
print(''.join(reversed(ans)))