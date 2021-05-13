h, w = list(map(int, input().split()))
# b = list(map(int, input().split()))
if h == 1 and w == 1:
    print(1)
elif h == 1:
    print(w-2)
elif w == 1:
    print(h-2)
else:
    print(h*w-h*2-(w-2)*2)
