# simple knapsack
n,W=map(int,input().split())
sacklist=[[]for i in range(4)]
w1=0
for _ in range(n):
    w,v=map(int,input().split())
    if _==0:
        w1=w
    sacklist[w-w1].append(v)

for i in range(4):
    sacklist[i].sort(reverse=True)
len1=len(sacklist[0])
len2=len(sacklist[1])
len3=len(sacklist[2])
len4=len(sacklist[3])
sumlist1=[]
sumlist2=[]
sumlist3=[]
sumlist4=[]
for _ in range(len1+1):
    sumlist1.append(sum(sacklist[0][:_]))
for _ in range(len2+1):
    sumlist2.append(sum(sacklist[1][:_]))
for _ in range(len3+1):
    sumlist3.append(sum(sacklist[2][:_]))
for _ in range(len4+1):
    sumlist4.append(sum(sacklist[3][:_]))
l1=len(sumlist1)
l2=len(sumlist2)
l3=len(sumlist3)
l4=len(sumlist4)
answer=0
for i in range(l1):
    for j in range(l2):
        for k in range(l3):
            for m in range(l4):
                if ((w1)*i+(w1+1)*j+(w1+2)*k+(w1+3)*m)<= W:
                    answer=max(answer,sumlist1[i]+sumlist2[j]+sumlist3[k]+sumlist4[m])
print(answer)
