s=list(input())
K=int(input())
substring=set()
alphabet=list('abcdefghijklmnopqrstuvwxyz')
l=0
while len(substring)<K:
    x=alphabet[l]
    l+=1
    for i in range(len(s)):
        if s[i]==x:
            string=s[i]
            substring.add(string)
            for k in range(1,5):
                try:
                    string+=s[i+k]
                    substring.add(string)
                except:
                    pass
ans=sorted(list(substring))
print(ans[K-1])