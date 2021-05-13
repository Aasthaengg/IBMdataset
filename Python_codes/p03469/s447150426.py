import sys
S = input()
if len(S) != 10:
    sys.exit()
if S[0:8] != '2017/01/':
    sys.exit()
if not (1 <= int(S[-2:]) <= 31):
    sys.exit()

print(S.replace('2017','2018'))
