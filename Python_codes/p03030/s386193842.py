#! env/bin/local python3
# -*- coding: utf-8 -*-

n = int(input())

restaurants = {}
for i in range(1, n + 1):
    info = input().split()
    restaurants[i] = {
        # 'name': info[0] + str(100 - int(info[1]))
        'name': info[0],
        'score': int(info[1])
    }

# {1: hoge} -> ([1, hoge])
results = sorted(restaurants.items(), key=lambda x: (x[1]['name'], 100 - x[1]['score']))
output = [r[0] for r in results]
print(*output, sep='\n')
