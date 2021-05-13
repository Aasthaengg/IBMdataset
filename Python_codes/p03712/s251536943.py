H, W = map(int, input().split())
a = ['#']*(W+2)
for i in range(H): a += [x for x in '#'+input()+'#']
a += ['#']*(W+2)
for i in range(0, (W+2)*(H+2), W+2):
    print(''.join(a[i:i+W+2]))
