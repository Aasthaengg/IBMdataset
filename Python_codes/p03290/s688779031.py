#https://atcoder.jp/contests/abc104/tasks/abc104_c

d,g=map(int,input().split())
l=[]
for i in range(d):
    l.append(list(map(int,input().split())))

set_all=set()
for i in range(d):
    set_all.add(i)


count=1001
for i in range(2**d):
    score=0
    count_buf=0
    set1=set()
    for j in range(d):
        if (i>>j)&1:
            score+=100*(j+1)*l[j][0]+l[j][1]
            count_buf+=l[j][0]
            set1.add(j)
    if score>=g:
        count=min(count,count_buf)
    else:
        set2=set_all-set1
        list_set2=list(set2)
        if len(list_set2)>0:
            list_set2.sort(reverse=True)
            for k in range(l[list_set2[0]][0]):
                score+=100*(list_set2[0]+1)
                count_buf+=1
                if score>=g:
                    count=min(count,count_buf)
                    break
    #print(score)
print(count)