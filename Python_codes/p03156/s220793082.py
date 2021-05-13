n=int(input())
a,b=map(int, input().split())
p=list(map(int, input().split()))

cnt1=0
cnt2=0
cnt3=0
for i in range(n):
    if p[i]<=a:
        cnt1+=1
    elif a<p[i]<=b:
        cnt2+=1
    else:
        cnt3+=1
print(min([cnt1,cnt2,cnt3]))
