#C
n,q = map(int,input().split())
s = input()
#累積和で考える
cnt = 0
cumsum = []
prev = s[0]
for i in range(n):
    now = s[i]
    if now == "C" and prev == "A":
        cnt += 1
    cumsum.append(cnt)
    prev = now
    
#print(cumsum)
for i in range(q):
    l,r = map(int,input().split())
    print(cumsum[r-1] - cumsum[l-1])