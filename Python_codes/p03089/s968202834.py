n=int(input())
s=list(map(int,input().split()))


result=[]

for i in range(n):
    posi=-1
    for index,ss in enumerate(s):
        if ss==index+1:
            posi=index
    if posi==-1:
        print(-1)
        exit()
    else:
        result.append(s[posi])
        s.pop(posi)

for item in result[::-1]:
    print(item)
    

