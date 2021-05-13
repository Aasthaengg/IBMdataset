tmp = '#.' * 151

def draw(H, W):
    odd = tmp[:W]
    even = tmp[1:W + 1]
    print((odd + '\n' + even + '\n') * (H // 2) + (odd  + '\n' if H % 2 else ''))
    
while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    draw(H, W)