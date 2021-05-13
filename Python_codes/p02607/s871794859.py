n = int(input())
a = list(map(int, input().split()))
ans=0
for index, value in enumerate(a):
    if (index+1) % 2 != 0:
        if value % 2 != 0:
            #print(value)
            ans+=1
print(ans)