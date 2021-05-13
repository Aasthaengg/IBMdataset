S = input()
N = len(S)

even_odd = [0, 0]
count_R = [0]*N
for i in range(N):
    if S[i] == 'R':
        even_odd[i%2] += 1
    if S[i] == 'L':
        count_R[i] += even_odd[i%2]
        count_R[i-1] += even_odd[1-i%2]
        even_odd = [0, 0]

S = S[::-1]
even_odd = [0, 0]
count_L = [0]*N
for i in range(N):
    if S[i] == 'L':
        even_odd[i%2] += 1
    if S[i] == 'R':
        count_L[i] += even_odd[i%2]
        count_L[i-1] += even_odd[1-i%2]
        even_odd = [0, 0]

count = [r+l for r, l in zip(count_R, count_L[::-1])]
print(' '.join(map(str, count)))