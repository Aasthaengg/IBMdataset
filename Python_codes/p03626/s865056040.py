
m = 1000000007

N = int(input())
S1 = input()
S2 = input()

state = ""
ans = 1
for n in range(N):
    s1, s2 = S1[n], S2[n]

    if s1 == s2:
        if state == "":
            ans = (ans*3) % m
        elif state == "tate":
            ans = (ans*2) % m
        state = "tate"
    else:
        if state == "yoko_continue":
            state = "yoko"
            continue
        elif state == "":
            ans = (ans*3*2) % m
        elif state == "tate":
            ans = (ans*2) % m
        elif state == "yoko":
            ans = (ans*3) % m
        state = "yoko_continue"

print(ans)
