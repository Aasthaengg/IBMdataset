a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
List=[a,b,c,d,e]
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[j]-List[i]>k:
            print(":(")
            exit()
print("Yay!")