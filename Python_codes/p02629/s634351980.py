n=int(input())
ans=[]
for i in range(1,99):
    if 26**i>=n:
        n-=1
        for j in range(i):
            key=chr(ord("a")+(n%26))
            ans.append(key)
            n=n//26
        break
    else:
        n-=26**i
        
ans.reverse()
for i in range(len(ans)):
    if i!=len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i])