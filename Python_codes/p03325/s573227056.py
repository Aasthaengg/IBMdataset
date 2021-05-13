import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

cnt = 0

def count_even(x):
    global cnt
    while x % 2 == 0:
        cnt += 1
        x //= 2

for i in a:
    count_even(i)

print(cnt)