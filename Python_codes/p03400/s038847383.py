n=int(input())
d,x=map(int,input().split())

eaten=0
for i in range(n):
    day=1
    a=int(input())
    while(day<=d):
        day+=a
        eaten+=1
print(eaten+x)