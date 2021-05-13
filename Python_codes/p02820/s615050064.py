def game(word):
    if word=="r":return p,"p"
    elif word=="s":return r,"r"
    else:return s,"s"


n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
ans=""

point=0
for i in range(n):
    num,word=game(t[i])
    if i<k:
        point +=num
        ans +=word
    else:
        if (t[i-k]==t[i] and ans[-k]!=word) or (t[i-k]!=t[i]):
            point +=num
            ans +=word
        else:
            ans +=t[i]

print(point)