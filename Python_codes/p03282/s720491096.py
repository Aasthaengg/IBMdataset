S = list(map(int, input()))
K = int(input())
if len(S) == 1:
    print(S[0])
    exit()

cnt = 0
for s in S:
    if s == 1:
        cnt += 1
    else:
        break

if K <= cnt:
    print(1)
else:
    print(S[cnt])
