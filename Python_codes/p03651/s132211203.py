n, k = list(map(int, input().split()))
al = list(map(int, input().split()))
flag = True
for a in al:
    if a >= k:
        flag = False
if flag:
    print('IMPOSSIBLE')
    exit()
# a,bの最大公約数


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


t = al[0]
for i in range(1, n):
    t = gcd(t, al[i])


for a in al:
    if abs(k-a) % t == 0:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
