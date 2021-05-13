N = int(input())
cnt = 0
st_cnt = 0
end_cnt =0
same_cnt =0

for k in range(N):
    s = input()
    cnt +=s.count("AB")

    if (s[0] =='B') & (s[-1]=='A'):
        same_cnt += 1
    elif (s[0] =='B'):
        st_cnt +=1
    elif (s[-1] == 'A'):
        end_cnt += 1
if same_cnt==0:
    print(cnt + same_cnt + min(st_cnt, end_cnt))
elif (st_cnt==0) and (end_cnt==0):
    print(cnt+same_cnt-1)
else:print(cnt+same_cnt+min(st_cnt,end_cnt))