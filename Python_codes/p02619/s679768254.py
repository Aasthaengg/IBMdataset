d=int(input())

last=[0]*26
c=list(map(int,input().split()))
s=[list(map(int, input().split())) for _ in range(d)]

t=[int(input()) for _ in range(d)]
ans=[]
score=0
for i in range(d):

    score+=s[i][t[i]-1]
    last[t[i]-1]=i+1
    for j in range(26):
        score-=(c[j]*((i+1)-last[j]))

        
    ans.append(score)


for item in ans:
    print(item)



