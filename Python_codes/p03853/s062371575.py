h,w=map(int,input().split())
s=[input() for i in range(h)]
for i in range(2*h):
    for j in range(w):
        if j==w-1:
            print(s[int(i)//2][j])
        else:
            print(s[i//2][j],end='')