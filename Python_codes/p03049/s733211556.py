N=int(input())
ans=0
cnt_a,cnt_b,cnt_c=0,0,0
for i in range(N):
    s=input()
    ans+=s.count("AB")
    s=s.replace("AB","")
    if s[0]=="B" and s[-1]=="A":
        cnt_c+=1
    elif s[0]=="B":
        cnt_b+=1
    elif s[-1]=="A":
        cnt_a+=1
if cnt_c==0:
    print(ans+min(cnt_a,cnt_b))
elif cnt_a+cnt_b == 0:
    print(ans+cnt_c-1)
else:
    print(ans+cnt_c+min(cnt_a,cnt_b))
