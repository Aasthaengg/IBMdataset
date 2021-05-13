import collections
H, W, M = map(int, input().split())

h, w = [0]*M, [0]*M
dic = set()
for i in range(M):
    h[i], w[i] = map(int, input().split())
    dic.add((h[i],w[i]))

counter = collections.Counter(h)
h_max = max(counter.values())
mode_h = [key for key , value in counter.items() if value == h_max]
counter = collections.Counter(w)
w_max = max(counter.values())
mode_w = [key for key , value in counter.items() if value == w_max]

for i in mode_h:
    for j in mode_w:
        if (i,j) not in dic:
            print(h_max+w_max)
            exit()

print(h_max+w_max-1)

