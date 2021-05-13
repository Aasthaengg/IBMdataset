S = input()
K = int(input())
t = -1
for k in range(len(S)):
    t = k
    if S[k] != "1":
        break
if K <= t:
    print(1)
else:
    print(S[t])
