a=int(input())
b,c=map(int,input().split())
d=list(map(int,input().split()))
result=[]
for i in d:
    result.append(b-i*0.006)
result2=[]
for i in result:
    result2.append(abs(c-i))
print(1+result2.index(min(result2)))
