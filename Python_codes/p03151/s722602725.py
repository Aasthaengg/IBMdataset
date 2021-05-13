n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

plus_l=[]
minus_l=[]
cnt=0
for i in range(n):
    if a[i]<b[i]:
        minus_l.append(b[i]-a[i])
        cnt+=1
    elif a[i]>b[i]:
        plus_l.append(a[i]-b[i])

if sum(minus_l)>sum(plus_l):
    print(-1)
    exit()

sum_minus=sum(minus_l)
tmp_sum_plus=0

plus_l.sort(reverse=True)

for p_i in plus_l:
    if tmp_sum_plus>=sum_minus:
        break
    tmp_sum_plus+=p_i
    cnt+=1
print(cnt)

