S = input()
N = len(S)
ans = []
check = []
for i in range(N):
    if S[i] != 'x':
        ans.append(S[i])
        check.append(i)
if len(ans) == 0:
    print(0)
    exit()
if ans != ans[::-1]:
    print(-1)
    exit()
if len(ans)%2:
    cl,cr = check[len(ans)//2],check[len(ans)//2]
else:
    cl,cr = check[len(ans)//2-1],check[len(ans)//2]
cnt = 0
while 0 <= cl and cr <= N-1:
    if S[cl] == S[cr]:
        cl -= 1
        cr += 1
    elif S[cl] == 'x':
        cnt += 1
        cl -= 1
    else:
        cnt += 1
        cr += 1
cnt += max(cl+1,N-cr)
print(cnt)
