X = input()

n = len(X)

S_cnt = 0
cnt = 0

for i in range(n):
    if X[i]=='S':
        S_cnt += 1
    elif (X[i]=='T') and(S_cnt>0):
        cnt += 1
        S_cnt -= 1
print(n-cnt*2)