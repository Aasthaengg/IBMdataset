N = int(input())
S = list(map(int, list(input())))
ans = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            targets = (a, b, c)
            target_idx = 0
            for i in range(len(S)):
                if S[i] == targets[target_idx]:
                    target_idx += 1
                    if target_idx == len(targets):
                        ans += 1
                        break

print(ans)
