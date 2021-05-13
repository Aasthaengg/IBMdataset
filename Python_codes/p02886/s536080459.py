n=int(input())
d_list=[int(i) for i in input().split()]
sum_list=[]


for i in range(n):
    for j in range(i+1,n):
        
        sum_list.append(d_list[i]*d_list[j])
        

print(sum(sum_list))
