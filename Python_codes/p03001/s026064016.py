W,H,w,h = map(float, input().split())
ans =0
if w+w ==W and h+h==H:
    ans =1
print('{:9f} {}'.format(W*H/2, ans))