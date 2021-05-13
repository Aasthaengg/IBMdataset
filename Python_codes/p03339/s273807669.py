n = int(input())
S = input()

E = [0] * n
W = [0] * n

for i in range(0, n):
    if i < n - 1:
        if S[i] == "W":
            E[i+1] = E[i] + 1
        else:
            E[i+1] = E[i]
        if S[n-i-1] == "E":
            W[n-i-2] = W[n-i-1] + 1
        else:
            W[n-i-2] = W[n-i-1]
min_so_far = n
for i in range(n):
    c = E[i]+ W[i]
    if min_so_far > c:
        min_so_far = c
print (min_so_far)