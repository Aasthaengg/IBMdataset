S = list(input())
ans = 'AC'
if not S[0] == 'A':
    ans = 'WA'
if not 'C' in (S[2:-1]):
    ans = 'WA'
if ans == 'AC':
    S.remove('A')
    S.remove('C')
    if not S == [s.lower() for s in S]:
        ans = ('WA')
print(ans)
