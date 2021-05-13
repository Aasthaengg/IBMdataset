N=int(input())
s=input()
r=0

for i in range(N):
    if s[i]=="R":
        r=r+1
if r>N-r:
    print("Yes")
else:
    print("No")
