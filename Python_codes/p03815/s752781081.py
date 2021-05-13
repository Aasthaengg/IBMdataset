#6→5を交互に上に向けるのが効率良い

n = int(input())
if n%11 == 0:
    print(n//11*2)
elif n%11 < 7:
    print((n//11)*2+1)
else:
    print((n//11+1)*2)