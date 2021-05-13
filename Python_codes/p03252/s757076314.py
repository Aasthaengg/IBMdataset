s=input()
t=input()
n=len(s)
s=sorted(s)
t=sorted(t)
Lists={}
nums=[]
Listt={}
numt=[]

for i in range(n):
    Lists.setdefault(s[i], 0)
    Listt.setdefault(t[i], 0)
    Lists[s[i]]+=1
    Listt[t[i]]+=1
    
for j in Lists.values():
    nums.append(j)
    
for j in Listt.values():
    numt.append(j)
#print(nums)
#print(numt)
#nums=sorted(Lists.values)
#numt=sorted(Listt.values)

if (sorted(nums)==sorted(numt)):
    print("Yes")
else:
    print("No")