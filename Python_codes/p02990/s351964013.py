#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:46:49 2020

@author: naoki
"""
N, K = map(int, input().split())
red_num = N-K

mod = 1000000007

kai = [1 for _ in range(2001)]
for i in range(2,2001):
    kai[i] = kai[i-1]*i%mod


for i in range(1,min(K, red_num+1)+1):
    place_option = kai[red_num+1]*pow(kai[i],mod-2,mod)*pow(kai[red_num+1-i],mod-2,mod)
    devide_option = kai[K-i+(i-1)]*pow(kai[K-i],mod-2,mod)*pow(kai[i-1],mod-2,mod)
    answer = (place_option%mod * devide_option%mod)%mod

    print(answer)

if red_num+1<K:
    for i in range(red_num+1,K):
        print(0)