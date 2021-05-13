x = input()
visited = [0]*(len(x))
ans = 0
s = 0
t = 0
for i in range(len(x)):
    if not visited[i]:
        if x[i:i+2] == "ST":
            ans += 2
            visited[i+1] = 1
        elif x[i] == "S":
            s += 1
        elif x[i] == "T" and s:
            ans += 2
            s -= 1
print(len(x)-ans)