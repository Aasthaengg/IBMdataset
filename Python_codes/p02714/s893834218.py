n = int(input())
s = input()

R=[]
G=[]
B=[]

for i in range(n):
    if s[i] == "R":
        R.append(i)
    elif s[i] == "G":
        G.append(i)
    else:
        B.append(i)

ans = len(R)*len(G)*len(B)
for i in range(n-2):
    for j in range(i+1,n-1):
        k  = 2*j-i
        if k<n:
            if (s[i]!=s[j]) and (s[i]!=s[k]) and (s[j]!=s[k]):
                ans-=1
print(ans)