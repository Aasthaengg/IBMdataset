

N = int(input())
S = str(input())
sum = 0
L = []
for i in range(N):
    if S[i] == "I":
        sum += 1
        L.append(sum)
    elif S[i] == "D":
        sum -= 1
        L.append(sum)

if max(L) > 0:
    print(max(L))

else:
    print(0)
