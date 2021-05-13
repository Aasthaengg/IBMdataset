import sys
n,k=map(int,input().split())
s=input()

if n == 1:
    print(0)
    sys.exit()

hap = 0
if s[0] == "R" and s[1] == "R":
    hap += 1
if s[-1] == "L" and s[-2] == "L":
    hap += 1

for i in range(1,n-1):
    if s[i] == "L" and s[i-1] =="L":
        hap += 1
    elif s[i] == "R" and s[i+1] == "R":
        hap += 1

rl = 0
lr = 0

for i in range(n-1):
    if s[i] == "L" and s[i+1] == "R":
        lr += 1
    elif s[i] == "R" and s[i+1] == "L":
        rl += 1

tmp = min(rl,lr,k)
hap += 2 * tmp

if s[0] != s[-1] and k - tmp >0:
    hap += 1
print(hap)