l, r = list(map(int, input().split()))
# A = list(map(int, input().split()))
#a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
#a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#x = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
# for i in range(1, int(n**0.5)+1):

mod = 2019
a = l//mod
b = r//mod

if b-a > 0:
    print(0)
else:
    m = 2020
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            a = (i*j) % mod
            if a < m:
                m = a

    print(m)
