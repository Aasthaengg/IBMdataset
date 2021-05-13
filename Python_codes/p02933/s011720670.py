# デバッグ用
GBN_DEBUG = False
def dprn(s, i):
    if GBN_DEBUG: print(", " + s + " = " + str(i), end = "")
def dprns(s):
    if GBN_DEBUG: print(", " + s, end = "")
def dprni(i):
    if GBN_DEBUG: print(i, end=" ")
def endl(): 
    if GBN_DEBUG: print('')
def puts(s): print(s)

#本体ここから

a = int(input())
s = input()
#S, T = input().split()
#N, M = map(int, input().split())
#W = [input() for _ in range(N)]
#A = list(map(int, input().split()))

#GBN_DEBUG = True

if a >= 3200:
    print(s)
else:
    print('red')
