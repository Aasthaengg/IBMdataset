n=int(input())
number_list=list(map(int,input().split()))
new_list=sorted(number_list,reverse=True)
#print(new_list)
alice_number=[]
for i in range(n):
    if i%2==1:
        continue
    alice_number.append(new_list[i])
#print(alice_number)
bob_number=[]
for i in range(n):
    if i%2==0:
        continue
    bob_number.append(new_list[i])
#print(bob_number)
result=sum(alice_number)-sum(bob_number)
print(result)