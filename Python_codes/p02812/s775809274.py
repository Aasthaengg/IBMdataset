n=int(input())
s=input()
cnt=0
for i in range(n-3+1):
    if s[i:i+3]=="ABC": cnt+=1
print(cnt)