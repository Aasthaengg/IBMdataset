n=int(input())
lst=list(input())
#i=0
ans_lst=[lst[1:].count("E")]

for i in range(1,n):
    temp_ans=ans_lst[i-1]
    if lst[i]=="E":
        temp_ans-=1
    if lst[i-1]=="W":
        temp_ans+=1
    ans_lst.append(temp_ans)

print(min(ans_lst))