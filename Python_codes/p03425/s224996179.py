import sys
input = sys.stdin.readline
n=int(input())

a="MARCH"
cnt=[0]*5
for i in range(n):
    s=input()
    for i in range(5):
        if s[0]==a[i]:
            cnt[i]+=1
ans=0
for i in range(3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      ans+=cnt[i]*cnt[j]*cnt[k]
print(ans)
