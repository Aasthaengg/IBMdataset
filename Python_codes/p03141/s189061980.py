import sys
input = sys.stdin.buffer.readline

from operator import itemgetter

N = int(input())
AB = []

for _ in range(N):
    A, B = map(int, input().split())
    AB.append([A, B, A+B])

AB.sort(key=itemgetter(2), reverse=True)

takahashi = True
ans = 0

for i in range(N):
    if takahashi:
        ans += AB[i][0]
    else:
        ans -= AB[i][1]
    takahashi = not takahashi

print(ans)