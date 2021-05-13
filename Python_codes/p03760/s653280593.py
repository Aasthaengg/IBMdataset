o=input()
e=input()
ans=[]
for i in range(len(o)):
    ans.append(o[i])
    if i < len(e):
        ans.append(e[i])
print(''.join(ans))