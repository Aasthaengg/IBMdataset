import sys
input = sys.stdin.readline
#n = int(input())
#l = list(map(int, input().split()))
'''
A=[]
B=[]
for i in range():
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)'''

n=int(input())
a = list(map(int, input().split()))
if (a[0]==1 and n+1>1) or a[0]>1:
    print(-1)
    sys.exit()
if n==0 and a[0]==1:
    print(1)
    sys.exit()

su=[0]*(n+1)
for i in range(1,n+1)[::-1]:
    su[i-1]+=su[i]+a[i]
#print(su)
yo_next=min(2-a[0],su[0])
cnt=yo_next+1

for i in range(1,n):
    if yo_next-a[i]<1:
        print(-1)
        sys.exit()
    
    yo_next=min(su[i],(yo_next-a[i])*2)
    cnt+=yo_next
    #print(cnt,su[i+1],(yo_next-a[i])*2)
if yo_next<a[-1]:
    print(-1)
    sys.exit()
else:
    print(cnt)