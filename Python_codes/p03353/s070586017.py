def cin():  return list(map(int,input().split()))

S = input()
k = cin()[0]
s = set()
length = len(S)
for i in range(length):
    tmp = ""
    for j in range(5):
        if i + j < length:
            tmp += S[i + j]
            s.add(tmp)
        
s = sorted(s)
ans = s[k - 1]
print(ans)