n, k = map(int, input().split())
s = input()
s1 = []
count = 0
if s[0] == "0":
    s1.append(0)
for i in range(n-1):
    if s[i+1] == s[i]:
        count += 1
    elif s[i+1] != s[i]:
        count += 1
        s1.append(count)
        count = 0
s1.append(count+1)
if s[-1] == "0":
    s1.append(0)

#print(s1)

# s1の累積和
s2 = [0]*(len(s1)+1)
s2[1] = s1[0]
for i in range(1, len(s1)):
    s2[i+1] = s1[i] + s2[i]
#print(s2)

ans = 0
if len(s2) > 2*k+1:
    for l in range(len(s2)-(2*k+1))[::2]:
        res = s2[2*k+1+l] - s2[l]
        ans = max(ans, res)
else:
    ans = s2[-1]
print(ans)