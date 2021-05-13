S=input()
pre="#"
cur=""
cnt=0

for s in S:
    cur+=s
    if pre!=cur:
        cnt+=1
        pre=cur
        cur=""
print(cnt)