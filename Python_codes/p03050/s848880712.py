import math
def prime_divisor(n):
    ls = []
    i = 2
    while i <= math.floor(n**0.5):
        if n%i == 0:
            ls.append(i)
            ls.append(n//i)
            i += 1
        else:
            i += 1
    if n > 1:
        ls.append(n)
    return ls
N = int(input())
ls1 = prime_divisor(N)
ls2 = [x-1 for x in list(set(ls1)) if x >= 2]
ls2.sort()
ls2.reverse()
ans = 0
for i in range(len(ls2)):
    if N // ls2[i] == N % ls2[i]:
        ans += ls2[i]
print(ans)