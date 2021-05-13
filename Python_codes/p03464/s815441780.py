import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
k=int(input())
a=list(map(int,input().split()))
min_num=2
max_num=3
for i in range(1,k):
    min_num=((min_num-1)//a[-i-1]+1)*a[-i-1]
    max_num=(max_num//a[-i-1]+1)*a[-i-1]-1

tmp=min_num
for i in range(k):
    tmp-=tmp%a[i]
if tmp!=2:
    print(-1)
    quit()

print(min_num)
print(max_num)