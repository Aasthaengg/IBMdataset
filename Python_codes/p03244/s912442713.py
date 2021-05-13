# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:36:13 2020

@author: NEC-PCuser
"""
n = int(input())
l = list(map(int, input().split()))
dic_gusu = {}
dic_kisu = {}

for i in range(0, n):
    if (i % 2 == 0):
        if (l[i] in dic_gusu):
            dic_gusu[l[i]] += 1
        else:
            dic_gusu[l[i]] = 1
    if (i % 2 == 1):
        if (l[i] in dic_kisu):
            dic_kisu[l[i]] += 1
        else:
            dic_kisu[l[i]] = 1
dic_kisu = sorted(dic_kisu.items(), key = lambda x : x[1])
dic_gusu = sorted(dic_gusu.items(), key = lambda x : x[1])

count = 0
if (len(dic_kisu) == 1 and len(dic_gusu) == 1 and dic_kisu[len(dic_kisu) - 1][0] == dic_gusu[len(dic_gusu) - 1][0]):
    count = n // 2
elif (dic_kisu[len(dic_kisu) - 1][0] != dic_gusu[len(dic_gusu) - 1][0]):
    for i in range(0, len(dic_kisu) - 1):
        count += dic_kisu[i][1]
    for i in range(0, len(dic_gusu) - 1):
        count += dic_gusu[i][1]
else:
    for i in range(0, len(dic_kisu)):
        count += dic_kisu[i][1]
    for i in range(0, len(dic_gusu)):
        count += dic_gusu[i][1]
    count_tmp = count
    count_ans = count_tmp - dic_kisu[len(dic_kisu) - 1][1] - dic_gusu[len(dic_gusu) - 2][1] 
    count_ans2 = count_tmp  - dic_kisu[len(dic_kisu) - 2][1] - dic_gusu[len(dic_gusu) - 1][1]
    count = min([count_ans, count_ans2])    
        
print(count)