n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
result = 0

for i in range(2**n):
    list_v = []
    list_c = []
    for j in range(n):
        if (i >> j) &1 ==1:
            list_v.append(v[j])
            list_c.append(c[j])
    if sum(list_v) - sum(list_c) >= result:
        result = sum(list_v) - sum(list_c)

print(result)