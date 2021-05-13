N=int(input())
S=input()
a='ABC'
x=0
y=0
for  i in range(N-2):
    x=0
    for j in range(3):
        if S[i+j]==a[j]:
            x+=1
        else:
            break
    if x==3:
        y+=1
print(y)