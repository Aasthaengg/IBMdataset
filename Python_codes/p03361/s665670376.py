import sys

H, W = map(int, input().split())
square = []
for i in range(H):
    a = list(map(str, input()))
    square += a

if H == W == 1:
    print('Yes')
    sys.exit()
    
for i in range(H*W):
    if square[i] == '#':
        if i % W != W-1:
            if square[i+1] == '#':
                continue
        if i % W != 0:
            if square[i-1] == '#':
                continue
            
        if i-W >= 0:
            if square[i-W] == '#':
                continue
        if i+W <= H*W:
            if square[i+W] == '#':
                continue
        print('No')
        sys.exit()
        
print('Yes')
            
