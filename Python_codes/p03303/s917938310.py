s=str(input())
k=int(input())
j=0
s1=''
for i in range(0,len(s),k):
    s1+=s[i]
print(s1)