from datetime import datetime
S = list(map(int,input().split('/')))

base = datetime(2019, 4, 30, 0, 0)
compare = datetime(S[0], S[1], S[2], 0, 0)

print('Heisei') if compare <= base else print('TBD')