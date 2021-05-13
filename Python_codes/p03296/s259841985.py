n=int(input())
a=list(map(int, input().split()))

sequence_num=a[0]
sequence_count=1
count=0

for i in range(1,n):
    if a[i]==sequence_num:
        sequence_count+=1
        if sequence_count%2==0:
            count+=1
    else:
        sequence_num=a[i]
        sequence_count=1
print(count)