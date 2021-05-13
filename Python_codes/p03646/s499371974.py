k=int(input())

ans=[i for i in range(50)]
for i in range(50):
    ans[-1-i]+=k//50
    
for i in range(k%50):
    ans[-1-i]+=1
    
print(50)
print(*ans)