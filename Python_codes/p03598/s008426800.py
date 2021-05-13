N_ko = int(input())
K = int(input())
x_s = list(map(int, input().split()))

ans_list = [min(abs(i - 0), abs(K - i)) for i in x_s]
ans = 2 * sum(ans_list)

print(ans)