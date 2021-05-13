n,m=map(int,input().split())
a=list(map(int,input().split()))
bc=[list(map(int, input().split())) for _ in range(m)]

sorted_ab=sorted(bc, reverse=True, key=lambda x: x[1])
new_ab=[]
ans=[]

for i in range(m):
    if len(new_ab)<=n:
        tmp_l=[sorted_ab[i][1]]*sorted_ab[i][0]
        new_ab+=tmp_l
    else:
        break

final_list=a+new_ab
final_list.sort(reverse=True)
print(sum(final_list[:n]))