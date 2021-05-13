n=int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
m=0
m+=l2[l1[0]-1]
for i in range(1,n):
    if l1[i] == l1[i-1]+1:
        m+=l2[l1[i]-1]+l3[l1[i]-2]
    else:
        m+=l2[l1[i]-1]
print(m)