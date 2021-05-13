# -*- coding: utf-8 -*-

H, W = map(int, input().split())
sh, sw = map(int, input().split())

print((H*W) - ((H*sw) + (W*sh) - (sw*sh)))

