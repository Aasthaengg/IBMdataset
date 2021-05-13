# -*- coding: utf-8 -*-
quest_num = int(input())
times = list(map(int, input().split()))

drink_num = int(input())

for i in range(drink_num):
    q, boost = map(int, input().split())
    print(sum(times) - times[q-1] + boost)

