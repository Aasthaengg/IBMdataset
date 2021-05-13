n,k,c = map(int, input().split())
s=input()
l=[-1] * k
r=[-1] * k
cnt=0
last=-float("inf")
for i in range(n):
    if last+c < i and s[i] == "o":
        last=i
        l[cnt]=i
        cnt+=1
        if cnt==k:
            break

cnt=0
last=float("inf")
for i in reversed(range(n)):
    if i < last-c and s[i] == "o":
        last=i
        r[cnt]=i
        cnt+=1
        if cnt==k:
            break

r=list(reversed(r))
for i in range(k):
    if l[i]==r[i]:
        print(l[i]+1)