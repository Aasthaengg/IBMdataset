stdin = open(0).read().split('\n')
H, W = map(int,stdin[0].split())
h, w = map(int,stdin[1].split())
print(H*W-H*w-h*W+h*w)