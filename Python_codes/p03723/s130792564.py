List=list(map(int,input().split()))
cnt=0
while(all(i%2==0 for i in List)):
    if List[0]==List[1]==List[2]:
        print(-1)
        exit()
    old_list=[List[0]//2,List[1]//2,List[2]//2]
    List[0]=old_list[1]+old_list[2]
    List[1]=old_list[0]+old_list[2]
    List[2]=old_list[0]+old_list[1]
    cnt+=1
print(cnt)