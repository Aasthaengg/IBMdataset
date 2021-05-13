# デバッグ用
GBN_DEBUG = False
GBN_DEBUG = True
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

#S = input()
#N = int(input())
#S, T = input().split()
N, K = map(int, input().split())
#W = [input() for _ in range(N)]
l = list(map(int, input().split()))

l.sort(reverse=1)
ans = 0
for i in range(K):
    ans += l[i]

print(ans)
