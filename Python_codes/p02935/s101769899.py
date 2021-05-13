N=int(input())
v=list(map(int,input().split()))
v_sort=sorted(v,reverse=False)
while len(v_sort)>1:
    v_sort=sorted(v_sort,reverse=False)
    v_sort.append((v_sort[0]+v_sort[1])/2)
    del v_sort[0]
    del v_sort[0]
print(*v_sort)