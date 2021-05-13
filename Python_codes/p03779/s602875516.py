x=int(input())
t=0
jump=0
for i in range(1,10**9):
    t+=1
    jump+=i
    if jump>=x:
        print(t)
        exit()