s = list(input())
k = int(input())
A = 'abcdefghijklmnopqrstuvwxyz'
Da = {a:i for i,a in enumerate(A)}

c = 0
for i in range(len(s)):
    if s[i]!='a' and 26-Da[s[i]]<=k:
        k -= 26-Da[s[i]]
        s[i] = 'a'
if k:
    s[i] = A[Da[s[i]]+k%26]
print("".join(s))