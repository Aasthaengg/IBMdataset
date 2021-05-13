A = {i-97:chr(i) for i in range(97,123)}
B = {v:k for k,v in A.items()}
s = list(input().strip())
K = int(input())
for i in range(len(s)-1):
    if s[i]!="a" and K>=26-B[s[i]]:
        K -= (26-B[s[i]])
        s[i]="a"
k = K%26
ind = (B[s[-1]]+k)%26
s[-1] = A[ind]
print("".join(s))