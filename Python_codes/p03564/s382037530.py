n=int(input())
k=int(input())
kk=n
p=1
while p < k:
    if kk == 0:
        break
    p*=2
    kk-=1
for i in range(kk):
    p+=k
print(p)