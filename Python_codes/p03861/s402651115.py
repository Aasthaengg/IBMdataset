import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)'''

a,b,x=map(int, input().split())

c=a//x
cc=b//x
if a%x==0:
    cc+=1
print(cc-c)