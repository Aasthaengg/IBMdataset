s=input()
ss='CODEFESTIVAL2016'
n=0
for i in range(len(s)):
    if s[i]!=ss[i]:
        n+=1
print(n)