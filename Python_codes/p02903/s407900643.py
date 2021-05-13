def print_ans():
    for i in field:
        print("".join(i))
    exit()
        
h,w,a,b=map(int,input().split())

field=[["0"]*w for i in range(h)]

if a==0:
    if b==0:
        print_ans()
    else:
        for i in range(b):
            field[i]=["1"]*w
        print_ans()
if b==0:
    for i in range(h):
        for j in range(a):
            field[i][j]="1"
    print_ans()
    
for i in range(h):
    for j in range(w):
        if i<b and j<a:
            field[i][j]="1"
        if i>=b and j>=a:
            field[i][j]="1"
print_ans()