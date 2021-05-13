l = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())
for i in range(n):
    b,f,r,v = [int(i) for i in input().split()]
    l[b-1][f-1][r-1] += v

for b in range(4):
    for f in range(3):
        out = ""
        for r in range(10):
            out += " " + str(l[b][f][r])
        print(out)
    if 3 != b:
        print("####################")
