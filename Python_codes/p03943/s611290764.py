# -*- coding: utf-8 -*-
candies = list(map(int, input().split()))

print('Yes' if (sum(candies) / 2) in candies else 'No')
