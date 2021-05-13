import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = list(map(int, input().split()))map(int, input().split())
    a.append(A)   
    b.append(B)'''

n,x=map(int, input().split())
a=list(map(int, input().split()))
ans=0
if a[0]>x:
    ans+=a[0]-x
    a[0]=x
#print(a)
for i in range(1,n):
    if a[i-1]+a[i]>x:
        ans+=a[i]-x+a[i-1]
        a[i]-=a[i]-x+a[i-1]
#        print(a)
print(ans)