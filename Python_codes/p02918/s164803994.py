n,k = map(int, input().split())
s=input()

init=0
if s[0] == "L":
    init+=1
if s[-1]=="R":
    init+=1

for i in range(n-1):
    if s[i]=="R" and s[i+1]=="L":
        init+=2

init -= 2*k
if init <= 0:
    init=1
print(n-init)