n=int(input())
chk=0
add=1
while chk<n:
    chk+=add
    add+=1
add-=1
if n==chk:
    for i in range(add):
        print(i+1)
else:
    exc=chk-n
    for i in range(add):
        if i+1==exc:
            continue
        print(i+1)