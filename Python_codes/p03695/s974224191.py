is_alive = [0]*8#各ランク

N = int(input())
a = list(map(int,input().split()))

count_over=0

for i in range(0,N,1):
    if a[i]>=3200:
        count_over +=1
    else:
        is_alive[a[i]//400]=1

print(max(1,sum(is_alive)),sum(is_alive)+count_over)