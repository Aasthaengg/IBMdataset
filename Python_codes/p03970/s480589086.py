S = input()
T = 'CODEFESTIVAL2016'
cnt=0
for s, t in zip(S, T):
    if s!=t:
        cnt+=1
print(cnt)