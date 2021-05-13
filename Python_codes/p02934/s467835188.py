n = int(input())
l = list(map(int, input().split()))
a = 0
for i in l:
    N = 1/i
    a += N
print(1/a)