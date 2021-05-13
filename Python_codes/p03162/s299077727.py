N=int(input())
a=0
b=0
c=0
a_list=[]
b_list=[]
c_list=[]
for i in range(N):
    a,b,c=map(int,input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
for i in range(1,N):
    a_list[i]=a_list[i]+max(b_list[i-1],c_list[i-1])
    b_list[i]=b_list[i]+max(a_list[i-1],c_list[i-1])
    c_list[i]=c_list[i]+max(a_list[i-1],b_list[i-1])
print(max(a_list[-1],b_list[-1],c_list[-1]))