n=int(input())
s=input()
ans=0
cnt={}
cnt["R"]=0
cnt["G"]=0
cnt["B"]=0
for i in s:
    cnt[i]+=1
ans = cnt["R"] * cnt["G"] * cnt["B"]
for i in range(n-2):
    for gap in range(1,(n-i+1)//2):
        if s[i] != s[i+gap] and s[i+2*gap] != s[i+gap] and s[i+2*gap] != s[i]:
            ans-=1
print(ans)