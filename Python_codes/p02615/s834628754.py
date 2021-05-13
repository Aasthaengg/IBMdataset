n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
sum_com = 0
distinct_a = sorted(list(set(a)), reverse=True)
comfort = {i: 0 for i in distinct_a}
comfort[a[0]] = 1
max_com = 0

for ai in a[1:]:
    sum_com += distinct_a[max_com]
    if distinct_a[max_com] == ai:
        comfort[distinct_a[max_com]] += 1
    else:
        comfort[distinct_a[max_com]] -= 1
        comfort[ai] += 2
        if comfort[distinct_a[max_com]] == 0:
            max_com += 1

print(sum_com)
