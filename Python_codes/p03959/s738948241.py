# 単調増加したらそこの山の高さは決まる。それ以外ならある高さ以内で自由に取れる。t,aで矛盾したら0
# 一人ずつ考えた
n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 1
MOD = 10**9 + 7
a_fixed = [-1] * n
t_fixed = [-1] * n

t_fixed[0] = t[0]
for i in range(1, n):
    if t[i] > t[i - 1]:
        t_fixed[i] = t[i]

a_fixed[-1] = a[-1]
for i in range(n - 2, -1, -1):
    if a[i] > a[i + 1]:
        a_fixed[i] = a[i]


for i in range(n):
    if t_fixed[i] != -1 and a_fixed[i] != -1:
        if t_fixed[i] != a_fixed[i]:
            print(0)
            exit()

    # 片方の制約を満たしているか
    elif t_fixed[i] != -1:
        if t_fixed[i] > a[i]:
            print(0)
            exit()
    elif a_fixed[i] != -1:
        if a_fixed[i] > t[i]:
            print(0)
            exit()
    else:
        ans *= min(a[i], t[i])
        ans %= MOD
# print(fixed)
print(ans)
