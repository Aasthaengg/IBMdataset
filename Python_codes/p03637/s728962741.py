N = int(input())
A = list(map(int,input().split()))

a_add=[]
a_2=[]
a_4=[]

for a in A:
    if a%2 != 0:
        a_add.append(a)
    if a%4 == 0: 
        a_4.append(a)
    elif a%2 == 0: 
        a_2.append(a)
        
# print(a_add,a_2,a_4)
        
ans='No'
if len(a_4) >= len(a_add):
    ans='Yes'
elif len(a_2)==0 and len(a_4) >= len(a_add)-1:
    ans='Yes'
print(ans)