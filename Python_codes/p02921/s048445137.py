s=input()
t=input()
cnt=0
for i,t in zip(s,t):
    if i==t:
        cnt+=1
print(cnt)