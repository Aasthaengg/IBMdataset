n, q = map(int, input().split())
S = input()
lr = []
s = [0]*(n+1)
count = 0

for i in range(q):
    LR = list(map(int, input().split()))
    lr.append(LR)

for i in range(n-1):
    if S[i:i+2] == "AC":
        count += 1
        s[i+1] = count
    else:
        s[i+1] = s[i]
        
for i in range(q):
    print(s[lr[i][1] - 1] - s[lr[i][0] - 1])