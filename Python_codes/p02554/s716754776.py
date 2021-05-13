#!/usr/bin/python3
#coding: utf-8

N = int(input())

p = 10**9 + 7

ret = pow(10, N, p)
ret -= pow(9, N, p)
ret -= pow(9, N, p)
ret += pow(8, N, p)

ret = (ret + p) % p

print(ret)