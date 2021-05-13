l = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = input()
for i in range(int(n)):
    b,f,r,v = input().split()
    #l[int(b)-1][int(f)-1][int(r)-1] = v
    l[int(b)-1][int(f)-1][int(r)-1] = l[int(b)-1][int(f)-1][int(r)-1] + int(v)

for b in range(4):
    for f in range(3):
        out = ""
        for r in range(10):
            out += " " + str(l[b][f][r])
        print(out)
    if 3 != b:
        print("####################")
