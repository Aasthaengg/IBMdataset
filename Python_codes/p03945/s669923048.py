S = input()
if S.count('B') == 0 or S.count('W') == 0:
    print(0)
    exit()
for _ in range(20):
    S = S.replace('BB','B').replace('WW','W')
print(len(S)-1)