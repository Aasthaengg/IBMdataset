N = int(input())
S = input()
d = {'R': 0, 'G': 0, 'B': 0}
for i in range(N):
    d[S[i]]+=1
tot = d['R']*d['G']*d['B']

counter = 0
for i in range(N):
    width = 1
    tmp = i+2
    while tmp < N:
        if S[i] != S[i+width] and S[i] != S[i+2*width] and S[i+width] != S[i+2*width]:
            counter += 1
        width += 1
        tmp = i + 2 * width
print(tot-counter)