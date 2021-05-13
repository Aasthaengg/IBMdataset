n = int(input())
s = []
for _ in range(n):
    s.append(input())

march=[0]*5
string="MARCH"

for i in range(n):
    for j in range(5):
        if s[i][0]==string[j]:
            march[j] +=1

if march.count(0)>=3:
    print(0)
    exit()

while march.count(0):
    march.remove(0)

ans=0
for i_0 in range(len(march)):
    for i_1 in range(i_0+1,len(march)):
        for i_2 in range(i_1+1,len(march)):
            ans = ans + march[i_0]*march[i_1]*march[i_2]
print(ans)
