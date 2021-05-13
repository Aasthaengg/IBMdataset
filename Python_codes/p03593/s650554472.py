H,W=map(int,input().split())
lines=[]
for i in range(H):
    lines.append(input().strip())

chars=dict()
for line in lines:
    for c in line:
        if c not in chars:
            chars[c]=0
        chars[c]+=1

def judge(H,W,chars):
    #両方奇数
    if H%2+W%2==2:
        ones=1
        twos=H//2 + W//2
    #両方偶数
    elif H%2+W%2==0:
        ones=0
        twos=0
    elif H%2==1:
        ones=0
        twos=W//2
    else:
        ones=0
        twos=H//2
    for c in chars:
        chars[c]%=4
        if chars[c]==0:
            continue
        if chars[c]==2:
            twos-=1
        elif chars[c]==3:
            twos-=1
            ones-=1
        else:
            ones-=1
    if ones<0 or twos<0:
        return False
    return True

if judge(H,W,chars):
    print("Yes")
else:
    print("No")