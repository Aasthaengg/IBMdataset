count = [[[0]*11 for j in range(4)] for i in range(5)]
n = int(input())

for i in range(n):
    b, f, r, v = map(int, input().split())
    count[b][f][r] += v

for b in range(1, 5):
    if b >= 2:
        print("####################")
    for f in range(1, 4):
        for r in range(1, 11):
            print(" ", count[b][f][r], end="", sep="")
        print()