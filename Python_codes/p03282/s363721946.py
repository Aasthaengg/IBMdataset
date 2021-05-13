S = list(input())
K = int(input())
a = 0


for i in range(len(S)):
    if S[i] == "1":
        a += 1
    else:
        break

if K <= a:
    print(1)
else:
    print(S[a])
