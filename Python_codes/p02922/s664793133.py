# -*- coding: utf-8 -*-
a, b = map(int, input().split())

socket = 1
tap_cnt = 0

while socket < b:
    socket -= 1
    socket += a

    tap_cnt += 1

print(tap_cnt)
