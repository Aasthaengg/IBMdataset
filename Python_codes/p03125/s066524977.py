A,B=map(int,input().split())
flag=0

for i in range(1,21):
    if B/A==i:
        flag+=1
        
if flag==0:
    print(B-A)
else :
    print(A+B)