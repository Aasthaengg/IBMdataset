A,B=map(int,input().split())
a=0
for i in range(A,B+1):
    if str(i)==''.join(list(reversed(str(i)))):
        a+=1
print(a)