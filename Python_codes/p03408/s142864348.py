n=int(input())
nlst=[input() for i in range(n)]
m=int(input())
mlst=[input() for i in range(m)]
ans=0
for i in nlst:
    plus=nlst.count(i)
    minus=mlst.count(i)
    ans=max(ans,plus-minus)
    
print(ans)