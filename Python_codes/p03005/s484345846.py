import math

#n = int(input())
n, k = [int(i) for i in input().split()]
#table = [[i for i in input().split()] for n in range(h)]
#table = [list(input()) for n in range(h)]
#list = [int(i) for i in input().split()]
#s = input()
#list = list(s)

#s = [int(input()) for i in range(m)] #mè¡1åå¥å

if (k == 1) :
    kotae = 0
else :
    kotae = n - k

print(kotae)