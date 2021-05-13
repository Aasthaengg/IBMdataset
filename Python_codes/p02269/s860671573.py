n = int(input())
o = {""}
for i in range(n):
    a = len(o)
    op, ob = map(str, input().split())
    if op == "find":
        o.add(ob)
        if len(o) > a:
            print("no")
            o.discard(ob)
        else:
            print("yes")
    else:
        o.add(ob)
