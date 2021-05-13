from itertools import combinations

n=int(input())
cnt=[0]*26

for i in range(n):
    s=input()
    cnt[ord(s[0])-ord('A')]+=1

ans=0

for c1,c2,c3 in combinations(["M","A","R","C","H"],3):
    c1=ord(c1)-ord("A")
    c2=ord(c2)-ord("A")
    c3=ord(c3)-ord("A")

    ans+=cnt[c1]*cnt[c2]*cnt[c3]

print(ans)