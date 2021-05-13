s=input()
k=int(input())
S=set()
for i in range(1,k+1):
    for j in range(len(s)):
        S.add(s[j:j+i])

print(sorted(S)[k-1])