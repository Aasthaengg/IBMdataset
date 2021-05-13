x=[]
for i in range(5):
    x.append(int(input()))
k=int(input())
ans="Yay!"
for j in range(5):
    for s in range(1,5):
        if j>=s:
            break
        if x[s]-x[j]>k:
            ans=":("
print(ans)