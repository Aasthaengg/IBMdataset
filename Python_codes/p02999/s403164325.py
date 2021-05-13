# coding: utf-8
# hello worldと表示
import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

x,a=MI()
if x<a:
    print(0)
else:
    print(10)