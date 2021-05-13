s=input()
k=int(input())
n=len(s)
i=0
ans=""
while i<n:
    if i!=n-1:
        if s[i]=="a":
            ans+="a"
            #print(ord(s[i]),123-ord(s[i]),k)
        elif k>=123-ord(s[i]):
            ans+="a"
            k-=(123-ord(s[i]))
            #print(ord(s[i]),123-ord(s[i]),k)
        else:
            ans+=s[i]
            #print(ord(s[i]),123-ord(s[i]),k)
    else:
        if k>=123-ord(s[i]):
            k-=(123-ord(s[i]))#一旦aにする
            k=k%26
            ans+=chr(97+k)
        else:
            ans+=chr(ord(s[i])+k)
        
    i+=1
print(ans)