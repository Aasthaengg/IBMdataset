from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

s=input()

key = "keyence"

for i in range(len(s)):
    j = i + len(s) -7
    if s[:i] + s[j:] == key:
        print("YES")
        exit()
print("NO")