n = int(input())
s = [input() for _ in range(n)]

march = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for name in s:
    if name[0] in march.keys():
        march[name[0]] += 1
#(m,a,r)(m,a,c)(m,a,h)
#(m,r,c)(m,r,h)
#(m,c,h)
ans = march['M']*march['A']*march['R']
ans += march['M']*march['A']*march['C']
ans += march['M']*march['A']*march['H']
ans += march['M']*march['R']*march['C']
ans += march['M']*march['R']*march['H']
ans += march['M']*march['C']*march['H']
#(a,r,c)(a,r,h)
#(a,c,h)
ans += march['A']*march['R']*march['C']
ans += march['A']*march['R']*march['H']
ans += march['A']*march['C']*march['H']
#(r,c,h)
ans += march['R']*march['C']*march['H']

print(ans)
