n = int(input())
a = list(map(int,input().split()))
head_s = [] 
back_s = []
n2 = 1
if n%2 == 0:
	n2 = 0
for h in range(n-1,-1,-2):
	head_s.append(a[h])
for b in range(n2,n,2):
	back_s.append(a[b])
#print(head_s,back_s)
ans_h = (' '.join(map(str,head_s)))
ans_b = (' '.join(map(str,back_s)))
print(ans_h,ans_b)