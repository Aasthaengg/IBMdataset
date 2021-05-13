s=input()
mozi=s[0]
count=0
for i in s:
    if i!=mozi:
        count+=1
        mozi=i
print(count)