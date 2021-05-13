import sys
input = sys.stdin.readline
li = [0,0,0,0]
for i in range(4) :
    li[i] = int(input())
print(min(li[0],li[1])+min(li[2],li[3]))