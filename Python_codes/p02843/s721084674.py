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

x=int(input())
ok=[1]+[0]*100000
ok[100]=1
if x<100:
    print(0)
    sys.exit()
a=[100,101,102,103,104,105]
for i in range(100,x+1):
    for item in a:
        if i-item>=0 and ok[i-item]==1:
            ok[i]=1
print(ok[x])