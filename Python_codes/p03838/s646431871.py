x, y = map(int, input().split())
ans = float('inf')

filt = lambda a: [ a, float('inf') ][ a < 0 ]

ans = min(ans, filt(   y  -    x )    )
ans = min(ans, filt(   y  - (- x)) + 1)
ans = min(ans, filt((- y) -    x ) + 1)
ans = min(ans, filt((- y) - (- x)) + 2)

print(ans)
