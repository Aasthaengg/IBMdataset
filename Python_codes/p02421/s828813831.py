n=int(input())
tp=0;hp=0
for i in range(n):
    t,h=input().split()
    if t>h:
        tp+=3
    elif t<h:
        hp+=3
    else:
        hp+=1;tp+=1
print(tp,hp)
