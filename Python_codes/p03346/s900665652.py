N=int(input())
data=[int(input()) for i in range(N)]
count=0
dic={}
for i in data:

    if i-1 in dic:
        num=dic.pop(i-1)
        dic.update({i:num+1})
    else:
        dic.update({i:1})
print(N-max([dic[i] for i in dic]))
