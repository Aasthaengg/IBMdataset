n=int(input())
arr=[int(i) for i in input().strip().split(" ")]
t=int(input())
dic={}
sum_array=0
for i in arr:
    dic[i]=dic.get(i,0)+1
    sum_array+=i
    

for _ in range(t):
    a,b=[int(i) for i in input().split(" ")]
    if a not in dic:
        print(sum_array)
        continue
    if b in dic:
        dic[b]+=dic[a]
    else:
        dic[b]=dic[a]
    
    sum_array+=dic[a]*(b-a)
    print(sum_array)
    dic[a]=0