N  = int(input())
x = map(int,input().split())
count=0
check = 0
NEW_x=[]

def roop(N,x):
    global check
    global NEW_x
    for i in x:
        s = i//2
        if i%2==0:
            check +=1
            
            NEW_x.append(s)


        else:
            NEW_x.append(s)

roop(N,x)

while True:
  
    x = NEW_x
    NEW_x = []
    if check ==N:
        check=0
        count+=1
        roop(N,x)
    else:
        break

print(count)