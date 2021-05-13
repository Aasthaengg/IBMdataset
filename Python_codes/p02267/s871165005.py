n = int(raw_input())
S = raw_input().split(" ")
q = int(raw_input())
T = raw_input().split(" ")

cnt = 0

for i in range(q):
    key = T[i]
    for j in range(n-1):
        if S[j] == key:
            cnt += 1
            break

print cnt