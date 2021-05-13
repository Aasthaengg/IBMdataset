a,b=map(int, input().split())
s=str(input())
b=b-1
slist=list(s)
if slist[b]=="A":
  slist[b]="a"
if slist[b]=="B":
  slist[b]="b"
if slist[b]=="C":
  slist[b]="c"
s="".join(slist)
print(s)