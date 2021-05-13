trump = {
        "S": list(range(1,14)),
        "H": list(range(1,14)),
        "C": list(range(1,14)),
        "D": list(range(1,14)),
        }
for i in range(0, int(input())):
    a,b = input().split()
    trump[a].remove(int(b))
for k in ["S","H","C","D"]:
    for e in trump[k]:
        print("{0} {1}".format(k, str(e)))