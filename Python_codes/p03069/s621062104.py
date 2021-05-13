import sys
input = sys.stdin.readline

N = int(input())
S = input()[:-1]
acc = [0]

for Si in S:
    if Si=='#':
        acc.append(acc[-1]+1)
    else:
        acc.append(acc[-1])

ans = 10**18

for i in range(N+1):
    ans = min(ans, acc[i]+N-i-(acc[N]-acc[i]))

print(ans)