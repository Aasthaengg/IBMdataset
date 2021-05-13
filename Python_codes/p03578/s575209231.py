import collections
n = int(input())
d_list = list(map(int, input().split()))
m = int(input())
t_list = list(map(int, input().split()))

if m > n:
    print("NO")
    exit()

d_c = collections.Counter(d_list)
t_c = collections.Counter(t_list)

for i in t_c:
    if t_c[i] <= d_c[i]:
        continue
    else:
        print("NO")
        exit()

print("YES")
