h,w,m=map(int, input().split())
hw=[list(map(int, input().split())) for _ in range(m)]

y_list=[0]*h
x_list=[0]*w

for h_i, w_i in hw:
    y_list[h_i-1]+=1
    x_list[w_i-1]+=1

my_cnt=max(y_list)
mx_cnt=max(x_list)

y_cnt=0
x_cnt=0

my_set=set()
mx_set=set()

for h_i, w_i in hw:
    if y_list[h_i-1]==my_cnt:
        my_set.add(h_i-1)
    if x_list[w_i-1]==mx_cnt:
        mx_set.add(w_i-1)

cnt=0
for h_i, w_i in hw:
    if y_list[h_i-1]==my_cnt and x_list[w_i-1]==mx_cnt:
        cnt+=1

print(my_cnt+mx_cnt-1 if cnt==len(my_set)*len(mx_set) else my_cnt+mx_cnt)
