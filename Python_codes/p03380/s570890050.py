n = int(input())
a_l = list(map(int,input().split()))

a_l.sort(reverse=True)
ans_n = a_l[0]
a_l2 = []
for i, val in enumerate(a_l):
    a_l2.append((abs(val-float(ans_n)/2),i))
a_l2.sort()

if a_l2[0][1] == 0:
    ans_r_index = a_l2[1][1]
else:
    ans_r_index = a_l2[0][1]
ans_r = a_l[ans_r_index]
print(ans_n, ans_r)