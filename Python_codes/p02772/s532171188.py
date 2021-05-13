n=int(input())

a_list=[int(i) for i in input().split()]

ans="APPROVED"
for i in a_list:
    if i%2==0:
        if i%3!=0 and i%5!=0:
            ans="DENIED"
            
print(ans)