from collections import defaultdict
n,m=map(int,input().split())
A=list(map(int,input().split()))
hon2=[1]
hon5=[2,3,5]
hon4=[4]
hon3=[7]
hon6=[6,9]
hon7=[8]
usenum=[]
usematch=defaultdict(int)
for a in A:
    if a in hon2:
        usenum.append(2)
        usematch[2]=max(a, usematch[2])
    if a in hon5:
        usenum.append(5)
        usematch[5]=max(a, usematch[5])
    if a in hon4:
        usenum.append(4)
        usematch[4]=max(a, usematch[4])
    if a in hon3:
        usenum.append(3)
        usematch[3]=max(a, usematch[3])
    if a in hon6:
        usenum.append(6)
        usematch[6]=max(a, usematch[6])
    if a in hon7:
        usenum.append(7)
        usematch[7]=max(a, usematch[7])
usenum=list(set(usenum))
usenum.sort()
dp=[-1]*(n+11)
dp[0]=0
for i in range(n+1):
    if dp[i]==-1:
        continue
    for num in usenum:
        dp[i+num]=max(10*dp[i]+usematch[num], dp[i+num])
print(dp[n])