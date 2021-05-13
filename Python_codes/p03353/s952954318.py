from string import ascii_lowercase
alp=ascii_lowercase
s=input()
k=int(input())
lst=set()
p=-1
while len(lst)<=k-1:
    p+=1
    for i in range(len(s)):
        if s[i]==alp[p]:
            for j in range(k):
                if i+j<len(s):
                    lst.add(s[i:i+j+1])
lst=sorted(lst)
print(lst[k-1])