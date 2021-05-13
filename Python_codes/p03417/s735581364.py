H,W = map(int, input().split())
h_ = (1 if H==1 else (0 if H == 2 else H-2))
w_ = (1 if W==1 else (0 if W == 2 else W-2))
ret = h_*w_
print(ret)