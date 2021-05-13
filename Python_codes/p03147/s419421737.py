n=int(input())
Tree_List=list(map(int,input().split()))
ct =0
for i in range(n):
    while Tree_List[i] != 0:
        k = i
        while Tree_List[k] != 0: 
            k+=1
            if k == n:
                break
        Tree_List[i:k]=map(lambda x:x-1,Tree_List[i:k])
        ct += 1
        
print(ct)