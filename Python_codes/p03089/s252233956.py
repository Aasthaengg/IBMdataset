N = int(input())
B = list(map(int, input().split()))
ORI_B = B[:]

ans = []
for i in range(N): # N回繰り返せば十分
    tgt = -1
    for i in reversed(range(len(B))):
        if B[i] == i+1:
            # B[i]をけす
            tgt = i
            break
    if tgt == -1:
        break
    ans.append(B[i])
    del B[i]

ans = ans[::-1]

if len(ans) == len(ORI_B):
    print('\n'.join(map(str, ans)))
else:
    print(-1)
