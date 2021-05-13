n,q=map(int,input().split())
s=input()

ac_num=0
ac_nums=[0]
for i in range(n-1):
    if s[i]=='A' and s[i+1]=='C':
        ac_num+=1
    ac_nums.append(ac_num)

for i in range(q):
    l,r=map(int,input().split())
    print(ac_nums[r-1]-ac_nums[l-1])
