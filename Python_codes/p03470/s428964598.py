N=int(input())
d=[]
for i in range(N):
    d.append(int(input()))
d.sort()
d.reverse()
sum=1
iii=d[0]
for i in range(N):
    if iii>d[i]:
        sum+=1
        iii=d[i]
print(sum)