x=[0]*5
for i in range(5):
    x[i]=int(input())
k=int(input())
ans=True
for i in range(5):
    for j in range(i+1,5):
        if abs(x[i]-x[j])>k:
            ans=False
            break
        
if ans==True:
    print("Yay!")
else:
    print(":(")

