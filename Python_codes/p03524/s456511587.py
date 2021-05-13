s=list(input())

a_cnt=s.count("a")
b_cnt=s.count("b")
c_cnt=s.count("c")
cnt=[a_cnt,b_cnt,c_cnt]
cnt.sort()

patarn= len(s)%3

if patarn==0:
    if a_cnt==b_cnt and b_cnt==c_cnt:
        print("YES")
    else:
        print("NO")
elif patarn==1:
    if cnt[0]==len(s)//3 and cnt[1]==len(s)//3 and cnt[2]==len(s)//3+1:
        print("YES")
    else:
        print("NO")
else:
    if cnt[0]==len(s)//3 and cnt[1]==len(s)//3+1 and cnt[2]==len(s)//3+1:
        print("YES")
    else:
        print("NO")

        

