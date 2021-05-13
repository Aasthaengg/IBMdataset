S=input()
K=int(input())
k=0
for s in S:
    k+=1
    if k==K:
        print(s)
        exit()
    if s!="1":
        print(s)
        break
else:
    print(1)