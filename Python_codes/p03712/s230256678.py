H,W = map(int,input().split())

ans = []

top = ['#']*(W+2)

ans.append(top)

for i in range(H):
    t = list(input())
    t = ['#'] + t + ['#']
    ans.append(t)

ans.append(top)

for aa in ans:
    print(''.join(map(str,aa)))