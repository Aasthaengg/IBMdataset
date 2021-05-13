building = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())

for _ in range(n):
    b, f, r, v = input().split(" ")
    building[int(b)-1][int(f)-1][int(r)-1] += int(v)



for i, b in enumerate(building):
    for f in b:
        for r in f:
            print(" %d"%(r), end="")
        print("")
    if i != 3:
        print ("#" * 20)