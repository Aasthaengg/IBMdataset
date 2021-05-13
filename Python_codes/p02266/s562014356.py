s=input()
s1=[]
s2=[]
ans=[]
a=0
a1=0
for i in range(len(s)):
    if s[i]=="\\":
        s1.append(i)
    elif s[i]=="/" and s1:
        i2=s1[-1]
        a1=i-i2
        a+=a1
        while s2 and s2[-1][0]>i2:
            a1+=s2[-1][1]
            s2.pop()
        s2.append([i2,a1])
        s1.pop()


n=len(s2)
for j in range(n):
  ans.append(s2[j][1])
print(a)
print(n,*(ans))
