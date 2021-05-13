n, k = map(int, input().split())
r, s, p = map(int, input().split())
T=list(input())

commands = [""]*n
ans = 0

for i, t in enumerate(T):
    if t == "p":
        command = "s"
        point = s
    elif t == "s":
        command = "r"
        point = r
    elif t == "r":
        command = "p"
        point = p

    if(i - k) >= 0 and (commands[i-k] == command):
        command = ""
        point = 0

    ans += point
    commands[i] = command
print(ans)
