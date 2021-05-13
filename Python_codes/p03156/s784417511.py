n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
cnt_1=0
cnt_2=0
cnt_3=0
for i in range(n):
	if p[i]<=a:
		cnt_1+=1
	elif p[i]<=b:
		cnt_2+=1
	else:
		cnt_3+=1
print(min(cnt_1,cnt_2,cnt_3))