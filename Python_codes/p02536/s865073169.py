N,M = map(int,input().split( ))
loads = []
teams = [[i] for i in range(N)]
syozoku = {i:i for i in range(N)}
for _ in range(M):
    A,B = map(int,input().split( ))
    if syozoku[A-1] != syozoku[B-1]:
        hairu,nukeru = min(syozoku[A-1],syozoku[B-1]),max(syozoku[A-1],syozoku[B-1])
        team = teams[nukeru]
        teams[nukeru] = []
        teams[hairu] += team
        for i in team:
            syozoku[i] = hairu

ans = -1
for team in teams:
    if len(team) != 0:
        ans += 1
print(ans)