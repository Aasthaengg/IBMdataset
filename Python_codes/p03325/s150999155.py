N = input()
a = list(map(int,input().split()))
ans=0
for x in a:
    if x%2!=0:
        continue
    for j in range(1,50):
        if x%2**j!=0:
            ans+=j-1
            break
print(ans)