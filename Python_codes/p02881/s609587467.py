N = int(input())

n_hoge = int(N ** 0.5)
print

true_ans = 10 ** 12
for i in range(1,n_hoge+1):
    if N % i == 0:
        ans = N // i
        true_ans = min(ans + i - 2, true_ans)

print(true_ans)