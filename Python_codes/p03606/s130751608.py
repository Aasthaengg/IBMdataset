import sys
input = sys.stdin.readline
sum = 0
N = int(input())
for i in range(N) :
    l,r = [int(i) for i in input().split()]
    sum += abs(r-l) +1
print(sum)