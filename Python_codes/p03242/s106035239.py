s=input()
ans=[]

for i in range(3):
    if s[i]=="1":
        ans.append(9)
    else:
        ans.append(1)

print(ans[2] + ans[1]*10 + ans[0]*100)