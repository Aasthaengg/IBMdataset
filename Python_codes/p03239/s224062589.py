N,T = map(int,input().split())
CT = [list(map(int,input().split())) for i in range(N)]
CT = list(filter(lambda x:x[1]<=T,CT))
if len(CT)==0:
    print('TLE')
else:
    print(min(CT)[0])