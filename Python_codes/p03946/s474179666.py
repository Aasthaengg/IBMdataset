n,t=map(int,input().split())
a=list(map(int,input().split()))


diff_v=0
max_a_v=0
max_a_pos=[]
aa=set([])
bb=set([])

for i in range(1,len(a)):
    index=len(a)-i-1
    if max_a_v<a[index+1]:
        max_a_v=a[index+1]
        max_a_pos=[index+1]
    elif max_a_v==a[index+1]:
        max_a_pos.append(index+1)

    if max_a_v-a[index]>diff_v:
        diff_v=max_a_v-a[index]
        aa=set([index])
        bb=set(max_a_pos)
    elif max_a_v-a[index]==diff_v:
        aa.add(index)
        bb|=set(max_a_pos)
    #print(a[index],max_a_v,diff_v,aa,bb)

print(min(len(list(aa)),len(list(bb))))


    

    


