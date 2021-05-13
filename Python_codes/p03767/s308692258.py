import sys

input = sys.stdin.readline
MOD = 1000000007

N = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)


res = 0

cnt = 0
i = 1
while (cnt < len(a)//3)  :
    res += a[i]
    i += 2
    cnt+=1

print(res)