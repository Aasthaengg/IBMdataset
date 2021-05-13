N, M = map(int, input().split())

Nl = [[] for i in range(N)]
# Pl = []

for i in range(M):
    P, Y = map(int, input().split())
    # Pl.append(P-1)
    Nl[P-1].append({"year": Y, "index": i, "pref": P-1})
newl = []
for i in Nl:
    i.sort(key=lambda x: x["year"])
    num = 1
    for j in i:
        j["order"] = num
        num += 1
    newl += i


newl.sort(key=lambda x: x["index"])

for i in newl:

    print("{:06}".format(i["pref"]+1), end="")
    print("{:06}".format(i["order"]))
