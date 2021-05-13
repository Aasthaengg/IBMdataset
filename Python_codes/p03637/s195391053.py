n = int(input())
a = list(map(int,input().split()))
odd = 0
mul2 = 0
mul4 = 0
for i in a:
    if i%4==0:mul4+=1
    elif i%2==0:mul2+=1
    else:odd+=1
ans = 'Yes'
if n==mul4+odd:
    if mul4+1<odd:ans='No'
else:
    if mul4<odd:ans='No'
print(ans)