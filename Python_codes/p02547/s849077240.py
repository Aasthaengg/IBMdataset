n=int(input())
q=[]
for _ in range(n):
    d_1,d_2=map(int,input().split())
    if d_1==d_2:
        q.append(1)
    else:
        q.append(0)
for i in range(n-2):
    if q[i]==q[i+1]==q[i+2]==1:
        print("Yes")
        exit()
print("No")