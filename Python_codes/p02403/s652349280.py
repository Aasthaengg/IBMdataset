# coding=utf-8

while True:
    height, width = map(int, raw_input().split())
    if height + width == 0:
        break
    else:
        print '\n'.join(['#' * width] * height) + '\n'