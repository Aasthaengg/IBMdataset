N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
war_flag = True

for z in list(range(X+1, Y+1)):
    if max(x) < z and min(y) >= z:
        war_flag = False
        break

if war_flag:
    print('War')
else:
    print('No War')