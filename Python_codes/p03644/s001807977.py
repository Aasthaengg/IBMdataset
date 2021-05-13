n=int(input())

count_list=[]
for i in range(1,n+1):
    count=0
    while True:
        
        if i%2==0:
            i//=2
            count+=1
        else:
            break
    count_list.append(count)

print(count_list.index(max(count_list))+1)