N = int(input())
a = list(map(int, input().split()))

xor = 0
for a_ in a:
    xor ^= a_

ans = []
for a_ in a:
    ans.append(str(xor ^ a_))

print(' '.join(ans))