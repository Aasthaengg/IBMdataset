building = {1:[],2:[],3:[],4:[]}
for b in range(1, 4+1):
    building[b] = [0 for i in range(3*10)]

n = int(input())
for i in range(n):
    b, f, r, v = list(map(int, input().split()))
    building[b][(f-1)*10+(r-1)] += v

for b in range(1, 4+1):
    for i in range(3):
        for j in range(10):
            print(" {0}".format(building[b][(i*10)+j]), end="")
        print()
    if b < 4:
        print("#"*20)