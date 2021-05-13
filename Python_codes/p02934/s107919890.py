n=int(input())
List=list(map(int,input().split()))
add=0
for i in List:
    add+=1/i
print(1/add)