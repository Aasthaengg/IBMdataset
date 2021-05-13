n = int(input())
#h, w, k = list(map(int, input().split()))
# A = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
p = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
# ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
p.sort()
a = p[n//2]
b = p[n//2-1]
if a == b:
    print(0)
else:
    print(a-b)
