n = int(input())
x_l = list(map(int,input().split()))
s_x_l = sorted(x_l)

med_idx = n//2
med_l = s_x_l[med_idx-1]
med_r = s_x_l[med_idx]

for i in range(n):
    if  x_l[i] <= med_l:
        print(med_r)
    else:
        print(med_l)