n=int(input())
p=[int(i) for i in input().split()]

count=0
for i in range(1, n-1):
    a=p[i-1]
    b=p[i]
    c=p[i+1]
    p_list=[a,b,c]
    #print(p_list)
    p_list.sort()
    
    if p[i]==p_list[1]:
        count+=1
        #print(p_list)
        
print(count)