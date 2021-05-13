n,ct = map(int, raw_input().split(' '))
m = min([u for u,v in [map(int,raw_input().split()) for _ in range(n)] if v <= ct] or [+float('inf')])
print 'TLE' if m == +float('inf') else m