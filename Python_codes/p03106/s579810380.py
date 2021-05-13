a,b,k=map(int, input().split())

w_list=[]

num=min(a,b)+1

for i in range(1,num):
    if a%i==0 and b%i==0:
        w_list.append(i)
        
w_list.sort(reverse=True)
print(w_list[k-1])