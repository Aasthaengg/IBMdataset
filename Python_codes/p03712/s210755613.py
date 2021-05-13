h, w = map(int, input().split())
e = []
for i in range(h):
    e.append(list(input()))
e.insert(0, ["#"] * (w + 2))
e[0] = "".join(e[0])
e.insert(len(e), ["#"] * (w + 2))
e[len(e)-1] = "".join(e[len(e)-1])
for i in range(h):
    e[i + 1].insert(0, "#")
    e[i + 1].insert(len(e[i + 1]), "#")
    e[i+1] = "".join(e[i+1])
for i in e:
    print(i)