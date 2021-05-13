s = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(raw_input())
for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    s[b-1][f-1][r-1] += v
for b in range(4):
    for f in range(3):
        print(" " + " ".join(map(str, s[b][f])))
    if b != 3:
        print("#"*20)