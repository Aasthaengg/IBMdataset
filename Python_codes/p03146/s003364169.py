s=int(input())
List=[]
List.append(s)
n=s
while(1):
    if List.count(n)>1:
        break
    if n%2==0:
        n=n//2
        List.append(n)
    else:
        n=3*n+1
        List.append(n)
print(len(List))