n, m = map(int, input().split())
s = input()
t = input()


def my_lcm(a, b):
    cum = a * b
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    # b がgcd になっている
    return cum // b


ans = my_lcm(n, m)
s_idx = 0
t_idx = 0
while s_idx < n and t_idx < m:
    if s[s_idx] != t[t_idx]:
        print(-1)
        exit()
    else:
        a = s[s_idx] + t[t_idx]
        t_idx += ans // n
        s_idx += ans // m
print(ans)
