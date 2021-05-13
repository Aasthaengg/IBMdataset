import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))

lst1.sort(reverse=True)

i = lst1[0]
lst1 = lst1[1:]

res = i/2
res2 = -1
minimum = 10**18
for j in lst1:
    if abs(j-res) < minimum:
        res2 = j
        minimum = abs(j-res)

print(i,res2)