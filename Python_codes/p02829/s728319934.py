a=int(input())
b=int(input())
ans=6
for i in range(1,4):
    if a==i or b==i:
            ans-=i
print(ans)