N = int(input())
S = input()
x = 0
ans = [x]
lis_S = list(S)

for i in range(N):
    if lis_S[i] == "I":
        x += 1
    else:
        x -= 1

    ans.append(x)

print(max(ans))
