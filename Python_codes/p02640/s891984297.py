X,Y=map(int,input().split())
now = 4*X
end = 2*X
while(now>=end):
    if now==Y:
        print("Yes")
        exit()
    now-=2
print("No")