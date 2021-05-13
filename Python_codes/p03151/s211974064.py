import heapq
n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
if sum(a_list)<sum(b_list):
    print(-1)
else:
    diff_list = [a_list[i]-b_list[i] for i in range(n)]
    posi_heap=[]
    heapq.heapify(posi_heap)
    cnt,diff_sum = 0,0
    for diff in diff_list:
        if diff<0:
            cnt+=1
            diff_sum+=diff
        elif diff>0:
            heapq.heappush(posi_heap,-1*diff)
    diff_sum*=(-1)
    i=0
    while diff_sum>0:
        diff_sum+=heapq.heappop(posi_heap)
        i+=1
    print(i+cnt)