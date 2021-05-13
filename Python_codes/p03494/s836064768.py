N = int(input())
src_list=sorted(list(map(int,input().split())))

cnt= 0
remaindar = list(map(lambda x:x % 2,src_list))
while (1 not in remaindar):
    src_list=list(map(lambda x:x/2,src_list))
    remaindar = list(map(lambda x:x % 2,src_list))
    cnt+=1

print(cnt)
