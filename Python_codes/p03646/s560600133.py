# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

#n = int(input())
#a = [int(i) for i in readline().split()]

k = int(input())

q,r = divmod(k,50)
c =q+49
a = [c-r]*(50-r) + [c+50-(r-1)]*r

print(50)
print(*a)




