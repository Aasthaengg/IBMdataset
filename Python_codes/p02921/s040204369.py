S = input()
N = input()

count = 0
for i in range(len(S)):
    if S[i] == N[i]:
        count += 1
print(count)