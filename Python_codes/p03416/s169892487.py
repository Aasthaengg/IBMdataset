A,B= map(int,input().split())

ans=0

for i in range(A,B+1):
    if str(i)[0]==str(i)[4] and str(i)[1]==str(i)[3]:
        ans +=1
    
print(ans)
