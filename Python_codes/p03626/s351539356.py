
N = int(input())
S1 = input()
S2 = input()


state = 0
now = 0
ans = 1

while now < N:

    if state == 0 and S1[now] == S2[now]:
        ans *= 3
        now += 1
        state = 1

    elif state == 0 and S1[now] != S2[now]:
        ans *= 6
        now += 2
        state = 2

    elif state == 1 and S1[now] == S2[now]:
        ans *= 2
        now += 1
        state = 1

    elif state == 1 and S1[now] != S2[now]:
        ans *= 2
        now += 2
        state = 2

    elif state == 2 and S1[now] == S2[now]:
        ans *= 1
        now += 1
        state = 1

    elif state == 2 and S1[now] != S2[now]:
        ans *= 3
        now += 2
        state = 2

    ans %= (10 ** 9 + 7)

print (ans)