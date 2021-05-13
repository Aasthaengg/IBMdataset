
N = int(input())

def dfs(x):
    if len(x) == N:
        s = "".join(chr(v + ord("a")) for v in x)
        print(s)
        return

    val = max(x)
    for i in range(val + 2):
        x.append(i)
        dfs(x)
        x.pop()

dfs([0])
