s=input()
n=len(s)
t=n-1
for i in range(n):
    if t>=4 and s[t-4:t+1]=="dream":
        t-=5
    elif t>=6 and s[t-6:t+1]=="dreamer":
        t-=7
    elif t>=4 and s[t-4:t+1]=="erase":
        t-=5
    elif t>=5 and s[t-5:t+1]=="eraser":
        t-=6
    else:
        break
    if t<0:
        break
if t==-1:
    print("YES")
else:
    print("NO")