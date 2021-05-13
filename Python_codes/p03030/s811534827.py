# -*- coding: utf-8 -*-

n = int(input())

shop = []
for i in range(n):
    s, p = input().split()
    p = int(p)

    shop += [{'idx': i+1, 'val':s+f'{100-p:03}'}]

shop_sorted = sorted(shop, key=lambda x:x['val'])

for shop in shop_sorted:
    print(shop['idx'])
