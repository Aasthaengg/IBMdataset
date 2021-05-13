X=int(input())
acc=0
cnt=0
t=0
while True:
    if acc>=X:
        break
    t+=1
    acc+=t
    cnt+=1
print(cnt)