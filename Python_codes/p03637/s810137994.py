n=int(input())
a=list(map(int, input().split()))
cnt_4=0
cnt_2=0
for i in range(n):
    if a[i]%4==0:
        cnt_4+=1
    elif a[i]%2==0:
        cnt_2+=1

print('Yes' if cnt_4*2+1>=n or (cnt_4*2+cnt_2>=n) else 'No')
