n, x = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# k = int(input())
L = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
d = 0
count = 1
for l in L:
    if d+l > x:
        break
    else:
        d = d+l
        count += 1

print(count)
