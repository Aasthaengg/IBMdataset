n=int(input())
if n%2==1:
    ans=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i<j:
                if not i+j==n:
                    ans.append([i,j])
    print(len(ans))
    for i in ans:
        print(i[0],i[1])
else:
    ans=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i<j:
                if not i+j==n+1:
                    ans.append([i,j])
    print(len(ans))
    for i in ans:
        print(i[0],i[1])
