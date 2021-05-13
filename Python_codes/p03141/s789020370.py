import sys
input=sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    sm = tmp[0] + tmp[1]
    l.append([tmp[0],tmp[1],sm])

l.sort(key=lambda x:x[2])
l.reverse()

t_sm=0
a_sm=0
cnt=0
for dish in l:
    if cnt%2==0:
        t_sm+=dish[0]
    else:
        a_sm+=dish[1]
    cnt+=1
print(t_sm-a_sm)