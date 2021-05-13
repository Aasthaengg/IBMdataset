N=int(input())

#       完全グラフ
#    1     14     -4
#    2     13     -3
#    3     12     -2
#    4     11     -1
#    5     10
#
#       完全グラフ
#    1     20     -6
#    2     19     -5
#    3     18     -4
#    4     17     -3
#    5     16     -2
#    6     15     -1

ans=[]
for i in range(1,N):
    for j in range(i+1,N+1):
        ans.append((i,j))
if N%2==0:
    for i in range(1,N//2+1):
        ans.remove((i,N+1-i))
else:
    for i in range(1,N//2+1):
        ans.remove((i,N-i))
print(len(ans))
for a in ans:
    print(a[0],a[1])
