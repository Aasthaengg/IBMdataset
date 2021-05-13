S=raw_input()
prev=""
cur=""
ans=0
for x in S:
    cur+=x
    if prev!=cur:
        ans+=1
        prev=cur
        cur=""
    else:
        pass
print ans