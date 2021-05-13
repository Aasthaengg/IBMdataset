N = int(input())
march = {'M':0, 'A':0, 'R':0, 'C':0, 'H':0}
for i in range(N):
    S = input()
    if S[0] == 'M':
        march['M'] += 1
    elif S[0] == 'A':
        march['A'] += 1
    elif S[0] == 'R':
        march['R'] += 1
    elif S[0] == 'C':
        march['C'] += 1
    elif S[0] == 'H':
        march['H'] += 1
ans = 0
ans += march['M']*march['A']*march['R']
ans += march['M']*march['A']*march['C']
ans += march['M']*march['A']*march['H']
ans += march['M']*march['R']*march['C']
ans += march['M']*march['R']*march['H']
ans += march['M']*march['C']*march['H']
ans += march['A']*march['R']*march['C']
ans += march['A']*march['R']*march['H']
ans += march['A']*march['C']*march['H']
ans += march['R']*march['C']*march['H']

print(ans)
