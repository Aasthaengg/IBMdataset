s = list(input())
n = len(s)
s_r = list(reversed(s))

cnt0 = 0
ss0 = False
for a,b in zip(s,s_r):
    if a == b:
        cnt0 += 1
    if cnt0 == len(s):
        ss0 = True

cnt1 = 0
ss1 = False
s1 =s[0:(n-1)//2]
s1_r = list(reversed(s1))
for a,b in zip(s1,s1_r):
    if a == b:
        cnt1 += 1
    if cnt1 == len(s1):
        ss1 = True
        
cnt2 = 0
ss2 = False
s2 =s[(n+3)//2-1:n]
s2_r = list(reversed(s2))
for a,b in zip(s2,s2_r):
    if a == b:
        cnt2 += 1
    if cnt2 == len(s2):
        ss2 = True
        
if ss0 and ss1 and ss2:
    print("Yes")
else:
    print("No")
