N = int(input())

ans = set()

for i in range(N):
    S = input()
    if S in ans:
        continue
    else:
        ans.add(S)

print(len(ans))