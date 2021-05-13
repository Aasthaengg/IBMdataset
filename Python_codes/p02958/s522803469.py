n=int(input())
p=list(map(int,input().split()))
cnt=0
sorted_p=sorted(p)
for i in range(len(p)):
    if p[i]!=sorted_p[i]:
        cnt+=1
if cnt<=2:
    print("YES")
else:
    print("NO")