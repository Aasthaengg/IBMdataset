n=int(input())
s=input()
w=s.count(".")
b=0
ans=10**9
for i in range(n):
    if w+b<ans: ans=w+b
    if s[i]==".": w-=1
    else: b+=1
if w+b<ans: ans=w+b
print(ans)