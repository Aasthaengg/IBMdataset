#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

H, W = 100, 100

def main():
    a, b = rli()
    grid = [['#' if j < H//2 else '.' for _ in range(W)] for j in range(H)]
    for i in range(a-1):
        x = i*2 % W
        y = (i*2 // W)*2
        grid[y][x] = '.'
    for i in range(b-1):
        x = i*2 % W
        y = 2*(i*2 // W)+H//2+1
        grid[y][x] = '#'
    print(H, W)
    for col in grid:
        print("".join(col))


if __name__ == '__main__':
    main()
