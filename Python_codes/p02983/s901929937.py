l,r=map(int, input().split())

k=0

can=[]
while l+k<=r and k<2020:
    can.append((l+k)%2019)
    k+=1
ans=2020
import itertools

for seq in itertools.combinations(range(len(can)),2):
    ans=min(ans,(can[seq[0]]*can[seq[1]])%2019)
print(ans)