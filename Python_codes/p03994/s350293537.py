s=input()
slist=[i for i in s]
K=int(input())
cost = []
for i in s:
    if i=="a":
        cost.append(0)
    else:
        cost.append(ord("z")-ord(i)+1)

for i,c in enumerate(cost):
    if c<=K:
        K = K-c
        slist[i]="a"

lastord = (ord(slist[-1])-ord("a")+K)%26+ord("a")
slist[-1]=chr(lastord)

print("".join(slist))