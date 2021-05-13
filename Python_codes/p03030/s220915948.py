n=int(input())
cnt=1
List=[]
for i in range(n):
    s,p=input().split()
    p=int(p)
    List.append([s,p,cnt])
    cnt+=1
List.sort()
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i][0]==List[j][0] and List[j][1]>=List[i][1]:
            List[i],List[j]=List[j],List[i]
for i in range(len(List)):
    print(List[i][2])