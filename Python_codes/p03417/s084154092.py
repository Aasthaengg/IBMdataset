h,w = map(int,input().split())
if h == w == 1:
    print(1)
if max(h,w) >= 2 and min(h,w) ==1:
    print(max(h,w) -2)
if max(h,w) >= 2 and min(h,w) ==2:
    print(0)
if max(h,w) >= 3 and min(h,w) >=3:
    print((h-2)*(w-2))
