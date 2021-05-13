H, W = map(int, input().split())
h, w = map(int, input().split())

allmenseki = H*W

kuro_yoko = h*W

kuro_tate = (H-h)*w

siro = allmenseki - (kuro_yoko + kuro_tate)

print(siro)
