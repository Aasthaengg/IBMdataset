n = int(input())
a = list(map(int, input().split()))
q = int(input())
xy = [map(int, input().split()) for _ in range(q)]
b, c = [list(i) for i in zip(*xy)]

ans = 0

sum_all = 0
for cnt in range(n):
    sum_all += a[cnt]

a = sorted(a)
list_a_num = [0]*(10**5 + 1)
for cnt in range(n):
    list_a_num[a[cnt]] += 1

for cnt in range(q):
    sum_all += (c[cnt] - b[cnt]) * list_a_num[b[cnt]]
    list_a_num[c[cnt]] += list_a_num[b[cnt]]
    list_a_num[b[cnt]] = 0
    print(sum_all)
