S,K=list(input()),int(input())
for i in S:
    K-=1
    if i!='1'or K==0:
        print(i)
        exit()