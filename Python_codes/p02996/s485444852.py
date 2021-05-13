n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[1])
#print(ab)
tot=0
for i in range(n):
    tot+=ab[i][0]
    if tot>ab[i][1]:
        print("No")
        exit()
print("Yes")