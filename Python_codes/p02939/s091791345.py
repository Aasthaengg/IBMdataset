s=input()
n=len(s)
l=[]
l.append(s[0])
i=1
k=0
while i < n:
    j=1

    if i==n-1 and l[k]==s[n-1]:
        break
    while l[k] == s[i:i+j]:
        j += 1

    l.append(s[i:i+j])
    i += j
    k += 1


print(k+1)
