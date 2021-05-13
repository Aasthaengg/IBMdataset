# ABC C-Tsundoku
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
an = list(map(int,input().split()))
bn = list(map(int,input().split()))

suma = [0]
sumb = [0]
a = 0
b = 0
for i in an:
    a += i
    suma.append(a)
for i in bn:
    b += i
    sumb.append(b)

res = [0]
l = m
for j in range(n+1):
    if k-suma[j] < 0:
        break
    while k-suma[j]-sumb[l] < 0 and l > 0:
        l -= 1
    res.append(j+l)
print(max(res))