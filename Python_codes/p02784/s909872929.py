#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	sys.stdin = open(name)

s,n = map(int,input().split())
l = list(map(int,input().split()))

if s<=sum(l):
    print("Yes")
else:
    print("No")

