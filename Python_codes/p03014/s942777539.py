h,w=map(int,input().split())
S=[]
for i in range(h):
    S.append(input())

tab=[[0 for i in range(w)] for q in range(h)]

cnt=0
for i in range(h):
    cnt=0
    for q in range(w):
        if S[i][q]==".":
            cnt+=1
        else:
            cnt=0
        tab[i][q]+=cnt



cnt=0
for i in range(h):
    cnt=0
    for q in range(w-1,-1,-1):
        if S[i][q]==".":
            cnt+=1
        else:
            cnt=0
        tab[i][q]+=cnt



cnt=0
for q in range(w):
    cnt=0
    for i in range(h):
        if S[i][q]==".":
            cnt+=1
        else:
            cnt=0
        tab[i][q]+=cnt



cnt=0
for q in range(w):
    cnt=0
    for i in range(h-1,-1,-1):
        if S[i][q]==".":
            cnt+=1
        else:
            cnt=0
        tab[i][q]+=cnt

print(max([max(col) for col in tab])-3)

