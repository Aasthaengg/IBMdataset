# Handstand

n, k = map(int, input().split())
s = list(str(input()))

t = [0]
cnt = 1
for i in range(n):
    if i==n-1 or s[i]!=s[i+1]:
        t.append(cnt)
        cnt = 1
    else:
        cnt += 1
t.append(0)

tsum = [0]*(len(t)+1)
for i in range(len(t)):
    tsum[i+1] = tsum[i] + t[i]

#print(tsum)

ans = 0
for i in range(1+int(s[0])%2, len(tsum)-2*k,2):
    tmp = tsum[i+2*k] - tsum[i-1]
    #print(tmp)
    ans = max(ans, tmp)

if ans==0:
    ans = len(s)
print(ans)
