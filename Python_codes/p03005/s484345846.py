import math

#n = int(input())
n, k = [int(i) for i in input().split()]
#table = [[i for i in input().split()] for n in range(h)]
#table = [list(input()) for n in range(h)]
#list = [int(i) for i in input().split()]
#s = input()
#list = list(s)

#s = [int(input()) for i in range(m)] #m行1列入力

if (k == 1) :
    kotae = 0
else :
    kotae = n - k

print(kotae)