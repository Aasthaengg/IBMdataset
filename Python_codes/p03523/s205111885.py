import sys
t="AKIHABARA"
old_s=input()
new_s=""
for c in old_s:
    if c!='A':
        new_s+=c
if new_s!="KIHBR":
    print('NO')
    sys.exit()
s=old_s
n=len(t)
for i in range(2**n):
    ans=""
    for j in range(n):
        if i&(1<<j):
            ans+=t[j]
    if ans==s:
        print('YES')
        sys.exit()
print('NO')