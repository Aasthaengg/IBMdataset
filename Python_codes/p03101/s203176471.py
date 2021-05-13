h,w = map(int,input().split())
erase_h,erase_w = map(int,input().split())

white_b = h*w

erase = erase_h*w + erase_w*h - (erase_h*erase_w)

print(white_b - erase)