#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	sys.stdin = open(name)

l = list(map(str,input().split()))
a,b = map(int,input().split())
check = input()

if check == l[0]:
    a -= 1
else:
    b -= 1

print(a,b)


