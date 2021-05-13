
import sys
sys.setrecursionlimit(1000000)

S=input()
s=[]
for i in S:
    s+=[i]
ans=0
que=[]
que+=[s[0]]
def cube(i):
    global ans
    if i==len(s):
        print(ans)
    else:
        que.append(s[i])
        flag=True
        while flag:
            if len(que)==0 or len(que)==1:
                flag=False
            elif que[-1]==que[-2]:
                flag=False
            elif que[-1]!=que[-2]:
                del que[-1]
                del que[-1]
                ans+=2
        cube(i+1)
cube(1)
