N = int(input())

a_dic = list(map(int, input().split()))

ans = [-1 for i in range(N)]

for i in range(N):
    num = N-i
    index = 2
    cnt = 0
    while num * index <= N:
        if ans[num*index -1] != -1:
            cnt += ans[num*index -1]
        index += 1
    if cnt % 2 == 1:
        if a_dic[num-1] == 1:
            ans[num-1] = 0
        else:
            ans[num-1] = 1
    else:
        if a_dic[num-1] == 1:
            ans[num-1] = 1
        else:
            ans[num-1] = 0



print(sum(ans))
for i in range(N):
    if ans[i] == 1:
        print(i+1)
