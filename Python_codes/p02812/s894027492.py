n=int(input())
l=input()
cnt=0
for i in range(n-2):
    if l[i]+l[i+1]+l[i+2]=="ABC":
        cnt+=1
print(cnt)