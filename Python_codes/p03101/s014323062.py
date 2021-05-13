def main(H,W,h,w):
    return (H-h)*(W-w)

H,W = map(int, input().split())
h,w = map(int, input().split())

print(main(H,W,h,w))