s=list(map(int,list(input())))
#print(s)
#modで考える
# 2019100を
# 2019100%2019 と100%1019
#同じmodの組み合わせ

#右から見ていく

mod=[0]*2019

tmp=0
ten=1

#hoge=""

for ii in range(len(s)):
    i=len(s)-ii-1
    if ii==0:
        ten=1
    else:
        ten=(ten*10)%2019

    tmp=((tmp+s[i]*ten)%2019)
    #hoge=str(s[i])+hoge
    #print(tmp,int(hoge)%2019,hoge)
    mod[tmp]+=1

ans=0
for i in range(2019):
    ans+=((mod[i]*(mod[i]-1))//2)

ans+=mod[0]

print(ans)

