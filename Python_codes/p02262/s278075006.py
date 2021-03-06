import sys
import math

ct= 0
def insertion_sort(a, n, g):
    global ct
    for j in range(0,n-g):
        v = a[j+g]
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j-g
            ct += 1
        a[j+g] = v

n = int(input())
a = list(map(int, sys.stdin.readlines()))
b = 701
g = [x for x in [1,4,10,23,57,132,301,701] if x <= n]
while True:
    b = math.floor(2.25*b)
    if b > n:
        break
    g.append(b)
g = g[::-1]

for i in g:
    insertion_sort(a, n, i)

print(len(g))
print(*g, sep=" ")
print(ct)
print(*a, sep="\n")