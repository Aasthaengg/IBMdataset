H, W = map(int, input().split())
a = [str(input()) for i in range(H)]
sharp = str("#"*(W+2))

Lists = []
Lists.append([sharp])
for i in range(H):
    Lists.append(["#" + a[i] +"#"])

Lists.append([sharp])

for List in Lists:
    print(*List)
