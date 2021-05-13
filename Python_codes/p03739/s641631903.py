n = int(input())
s = list(map(int,input().split()))

temp = 0
cand1 = 0
for i in range(n):
    temp += s[i]
    if i%2 == 0:#正になってほしい
        if temp <= 0:
            cand1 += abs(temp-1)
            temp = 1
    else:#負になって欲しい
        if temp >= 0:
            cand1 += abs(temp+1)
            temp = -1

temp = 0
cand2 = 0
for i in range(n):
    temp += s[i]
    if i%2 == 0:
        if temp >= 0:
            cand2 += abs(temp+1)
            temp = -1
    else:
        if temp <= 0:
            cand2 += abs(temp-1)
            temp = 1

print(min(cand2,cand1))
