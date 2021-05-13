from collections import defaultdict

H,W = map(int, input().split())
cnt = defaultdict(int)
for _ in range(H):
    for a in list(input()):
        cnt[a] += 1
cnt = [c for c in cnt.values()]



for i in range((H + 2 - 1) // 2):
    for j in range((W + 2 - 1) // 2):
        need = [(i, j), (H - 1 - i, j), (i, W - 1 - j), (H - 1 - i, W - 1 - j)]
        need = set(need)

        cnt.sort()

        flag = False
        for k in range(len(cnt)):
            if len(need) <= cnt[k]:
                flag = True
                cnt[k] -= len(need)
                if cnt[k] == 0:
                    cnt.pop(k)
                break
                    
        if not flag:
            print("No")
            exit()

print("Yes")