import bisect
import sys
input = sys.stdin.readline


n, q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(n)]
events.sort(key=lambda x: x[2])

departures = [int(input()) for _ in range(q)]


ans = ['-1'] * q
skip = [-1] * q

for start, end, pos in events:
    left = bisect.bisect_left(departures, start-pos)
    right = bisect.bisect_left(departures, end-pos)

    while left < right:
        if skip[left] == -1:
            ans[left] = str(pos)
            skip[left] = right
            left += 1

        else:
            left = skip[left]

print('\n'.join(ans))
