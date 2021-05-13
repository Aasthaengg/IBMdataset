n=int(input())
L=list(map(int,input().split()))
num=1
min_num=0
for i in range(n):
    if i==0:
        min_num=L[0]

    elif min_num>=L[i]:
        num+=1
        min_num=L[i]

print(num)
