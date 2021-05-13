n = input()
S = map(int, raw_input().split())
q = input()
T = map(int, raw_input().split())

count = 0

for i in range(q):
    Search = T[i]
    for j in range(n):
        if S[j] == Search:
            count = count + 1
            break

print count