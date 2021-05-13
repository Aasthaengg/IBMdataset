#coding: utf-8

N = input()
A = [int(x) for x in input().split()]

print(sum(x-1 for x in A))
