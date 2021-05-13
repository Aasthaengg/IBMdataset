s=input()
ans=0
def dfs(i,stri,sum): #i個土入れてstriを作ってる、和は？
    global ans
    #print(i,stri,sum)
    if i==3 and sum==7:
        #print("ore")
        ans=stri+"=7"
        
    
    if i<=2:
        dfs(i+1, stri+ f"+{s[i+1]}" , sum+int(s[i+1]))
        dfs(i+1, stri+ f"-{s[i+1]}", sum-int(s[i+1]))

dfs(0,s[0],int(s[0]))
print(ans)