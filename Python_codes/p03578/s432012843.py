from collections import Counter
n = int(input())
d_li = list(map(int,input().split()))
m = int(input())
t_li = list(map(int,input().split()))

d_counter = Counter(d_li)
t_counter = Counter(t_li)
t_most_counter = t_counter.most_common()
t_len = len(t_most_counter)
for i in range(t_len):
    dum = t_most_counter[i][0]
    if d_counter[dum] >= t_most_counter[i][1]:
        pass
    else:
        print("NO")
        exit()
print("YES")