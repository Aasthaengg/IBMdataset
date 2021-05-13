import itertools
n=int(input())
name=dict()
for c in "MARCH":
    name[c]=0
for i in range(n):
    t=input()
    if t[0] in "MARCH":
        name[t[0]]+=1

ans=0
for hey in itertools.combinations("MARCH",3):
    ans+=name[hey[0]]*name[hey[1]]*name[hey[2]]
print(ans)