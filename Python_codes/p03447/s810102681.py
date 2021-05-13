X,A,B=[int(input()) for i in range(3)]
x=0
XX=X-A
while XX>=0:
    XX-=B
    x+=1

print(X-A-B*(x-1))