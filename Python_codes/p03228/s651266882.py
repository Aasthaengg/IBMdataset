#Tenka1 Programmer Beginner Contest b
def move(me,you):
    if me%2==0:
        return me//2,you+me//2
    else:
        return (me-1)//2,you+(me-1)//2

a,b,k=map(int,input().split())
turn=True#takahashi true aoki false
cnt=0
while cnt<k:
    if turn:
        a,b=move(a,b)
        cnt+=1
        turn=False
    else:
        b,a=move(b,a)
        cnt+=1
        turn=True
print(a,b)
