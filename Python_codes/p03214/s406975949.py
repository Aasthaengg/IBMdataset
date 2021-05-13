import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
a = [int(i) for i in input().split()]

avg = sum(a) / N
mk, mv = 0, float('inf')
for i in range(N) :
    if abs(a[i]-avg) < mv :
        mk, mv = i, abs(a[i]-avg)
print(mk)