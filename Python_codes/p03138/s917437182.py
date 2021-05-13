import copy
N,K = map(int,input().split())
lis = list(map(int,input().split()))
final = copy.copy(lis)
count = []
ans_K = 0
ans = 0
for i in range(1,41):
    check = 0
    for j in range(N):
        if lis[j]%2 != 0:
            check += 1
        if lis[j] == 1:
            lis[j] =0
        lis[j] = lis[j]//2
    if check >= N//2 +1:
        count.append(0)
    else:
        count.append(1)
count.reverse()
for k in range(len(count)):
    if count[k] == 1:
        if ans_K +(2 ** (len(count)-k-1)) <=K:
            ans_K += 2 ** (len(count)-k-1)
for l in final:
    ans += ans_K^l
print(ans)