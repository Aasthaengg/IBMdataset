s1,s2,s3,s4 = list(input())
p=0
if s1==s2 and s2== s3 and s3==s4:
    p=1
elif s1==s2:
    if s3!=s4:
        p=1
elif s1==s3:
    if s2!=s4:
        p=1
elif s1==s4:
    if s3!=s2:
        p=1
else:
    p=1
if p==0:
    print("Yes")
elif p==1:
    print("No")
