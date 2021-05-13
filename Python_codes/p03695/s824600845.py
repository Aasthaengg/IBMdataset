n = int(input())
a = list(map(int,input().split()))
col = [0]*8
over_cnt = 0
cnt_min = 0
cnt_max = 0
for i in range(n):
	if a[i] < 3200:
		col[(a[i])//400] += 1
		#print(col)
	else:
		over_cnt += 1
for j in range(8):
	#print(j)
	if col[j] > 0:
		cnt_min += 1
if cnt_min == 0:
	cnt_min = 1
	cnt_max = over_cnt
else:
	cnt_max = cnt_min+over_cnt
print(cnt_min,cnt_max)