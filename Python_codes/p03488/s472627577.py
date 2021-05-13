#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()
    X, Y = map(int, input().split())
    Dxy = [[] for _ in range(2)]
    cnt = 0
    direc = 0
    for x in S:
        if x == 'F':
            cnt += 1
        else:
            Dxy[direc].append(cnt)
            cnt=0
            direc = 1-direc
    Dxy[direc].append(cnt)

    Dx = Dxy[0][1:]
    Dy = Dxy[1]
    dpx=[set([Dxy[0][0]]),set([])]
    dpy=[set([0]),set([])]
    i=1
    for dx in Dx:
        dpx[i]=set([])
        for x in dpx[1-i]:
            dpx[i].add(x+dx)
            dpx[i].add(x-dx)
        i = 1-i
    j=1
    for dy in Dy:
        dpy[j]=set([])
        for y in dpy[1-j]:
            dpy[j].add(y+dy)
            dpy[j].add(y-dy)
        j = 1-j

    if X in dpx[1-i] and Y in dpy[1-j]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()