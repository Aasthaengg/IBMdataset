a=list(map(int,input().split()))

a.sort()

answer=((a[2]-a[1])+(a[2]-a[0]))/2
if ((a[2]-a[1])+(a[2]-a[0]))%2!=0:
    answer+=1.5

print(int(answer))