a='CODEFESTIVAL2016'
s=input()
cnt=0
for i,j in zip(a,s):
    if i!=j:
        cnt+=1
print(cnt)