n = int(input())
s = input()
b_lst=[]
w_lst=[]
b_cnt=0
w_cnt=0
for i in range(len(s)):
    b_lst.append(b_cnt)
    w_lst.append(w_cnt)
    if s[i]=="#":
        b_cnt+=1
    if s[len(s)-i-1]==".":
        w_cnt+=1
b_lst.append(b_cnt)
w_lst.append(w_cnt)
w_lst.reverse()

ans=10**9
for b,w in zip(b_lst,w_lst):
    if ans > b+w:
        ans=b+w
print(ans)