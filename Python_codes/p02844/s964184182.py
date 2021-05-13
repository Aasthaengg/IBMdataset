def find(fr, target):
    for i in range(fr, len(S)):
        if S[i] == target:
            return i
    return -1

N = int(input())
S = input()
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            now = find(0, str(i))
            if now == -1: continue
            now = find(now+1, str(j))
            if now == -1: continue
            now = find(now+1, str(k))
            if now == -1: continue
            ans += 1
print(ans)
