import sys
def input(): return sys.stdin.readline().strip()
b=input()
n=len(b)
l=[""]*n
for i in range(n):
    if b[i]=="A":
        l[i]="T"
    if b[i]=="T":
        l[i]="A"
    if b[i]=="G":
        l[i]="C"
    if b[i]=="C":
        l[i]="G"
print(*l)