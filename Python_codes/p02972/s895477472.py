N = int(input())
a = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    tmp = N - i
    kosuu = N // tmp
    if kosuu == 1:
        if a[tmp-1] == 1:
            ans[tmp-1] = 1
    else:
        sub_sum = 0
        for j in range(kosuu-1):
            sub_sum += ans[tmp * (j + 2) -1]
        if a[tmp-1] != sub_sum % 2:
            ans[tmp-1] = 1
            
true_ans = []
for i in range(N):
    if ans[i] == 1:
        true_ans.append(i + 1)
print(sum(ans))
print(*true_ans)