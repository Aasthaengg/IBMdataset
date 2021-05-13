import sys
def input():
    return sys.stdin.readline()[:-1]
a=input()
li=[0]*26
for i in range(len(a)):
    li[ord(a[i])-ord("a")]+=1
ans=len(a)*(len(a)-1)//2+1
for i in li:
    ans-=i*(i-1)//2
print(ans)