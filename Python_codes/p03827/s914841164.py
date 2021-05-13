N = int(input())
S = input()

cnt = 0
res = 0
for i in range(N):
    if S[i] == 'I':
        cnt +=1
    else:
        cnt -=1
    if cnt > res:
        res = cnt
print(res)