l=int(input())
n=input()
ans=0
for i in range(len(n)-2):
    if n[i:i+3]=="ABC":
        ans+=1
print(ans)