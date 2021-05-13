s=input()
count=0
n=int(len(s))
t1=s[:int((n-1)/2)]
t2=s[int((n+3)/2-1):]
result='No'
if s==s[::-1]:
    if t1==t1[::-1]:
        if t2==t2[::-1]:
            result='Yes'
print(result)
