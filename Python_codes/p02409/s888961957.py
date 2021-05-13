building = [[[0 for i in range(10)] for i in range(3)]for i in range(4)]

n = input()

for i in range(n):
    b,f,r,v = map(int,raw_input().split())
    building[b-1][f-1][r-1] += v

for B in range(4):
    for F in range(3):
        print " "+ " ".join(map(str,building[B][F]))
    if B != 3:
        print "#"*20