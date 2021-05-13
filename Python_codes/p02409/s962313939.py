n = int(raw_input())
 
info = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
 
for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    b, f, r = b-1, f-1, r-1
    info[b][f][r] += v
 
sharp = False
for i in info:
    if sharp:
        print "#" * 20
    for j in i:
        print " "+" ".join(map(str, j))
    sharp = True