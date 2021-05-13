P = 10**9 + 7
N = int(input())
S = input()

d = [0]*26
for s in S:
    d[ord(s)-97] += 1

ans = 1
for num in d:
    ans *= (num+1)
    ans %= P
print((ans-1)%P)