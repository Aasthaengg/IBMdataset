def main():

    s = str(input())
    x, y = map(int, input().split())

    n = len(s)

    dir = 1
    dx = []
    dy = []
    cnt = 0
    for i in range(n):
        if s[i] == 'F':
            cnt += 1
        else:
            if dir == 1:
                dx.append(cnt)
                cnt = 0
                dir = -1
            else:
                dy.append(cnt)
                cnt = 0
                dir = 1
    else:
        if dir == 1:
            dx.append(cnt)
        else:
            dy.append(cnt)
    #print(dx)
    #print(dy)
    D = 8000*2+1

    import numpy as np
    dpx = [0]*(len(dx)+1)
    dpy = [0]*(len(dy)+1)
    dpx[0] = np.zeros(D, np.bool)
    dpy[0] = np.zeros(D, np.bool)
    dpx[0][8000] = 1
    dpy[0][8000] = 1
    for i, d in enumerate(dx):
        if i == 0:
            b = np.zeros(D, np.bool)
            b[d:] |= dpx[i][:D-d]
            dpx[i+1] = b
        else:
            b = np.zeros(D, np.bool)
            b[d:] |= dpx[i][:D-d]
            b[:D-d] |= dpx[i][d:]
            dpx[i+1] = b

    for i, d in enumerate(dy):
        b = np.zeros(D, np.bool)
        b[d:] |= dpy[i][:D-d]
        b[:D-d] |= dpy[i][d:]
        dpy[i+1] = b

    if dpx[-1][8000+x] == 1 and dpy[-1][8000+y] == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
