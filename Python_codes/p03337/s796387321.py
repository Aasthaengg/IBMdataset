A,B=map(int,input().split())

li=[]

li.append(A+B)
li.append(A-B)
li.append(A*B)

ans=sorted(li)

print(ans[2])
