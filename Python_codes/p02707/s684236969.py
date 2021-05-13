n = int(input())
A = list(map(int, input().split()))

ans = [0] * n

for a in A:
    a -= 1
    ans[a] += 1

print('\n'.join(map(str, ans)))