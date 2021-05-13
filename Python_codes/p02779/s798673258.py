n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
if(len(s)==n):
    print("YES")
else:
    print("NO")