h,w,a,b = map(int,input().split())
s = [['0' for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if (i < b and j >= a) or (i >= b and j < a):
            s[i][j] = '1'
    print(''.join(map(str,s[i])))