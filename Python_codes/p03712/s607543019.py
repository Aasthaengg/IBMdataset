h, w = map(int, input().split())
l = [list(map(str, input().split())) for i in range(h)]
l = [["#"] + l[i] + ["#"] for i in range(h)]
l = [["#" for i in range(w+2)]] + l + [["#" for i in range(w+2)]]
for i in range(h+2):
    print("".join(l[i]))