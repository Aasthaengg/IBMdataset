S=input()
A='abcdefghijklmnopqrstuvwxyz'
N=len(S)

ans='-1'
if N<26:
    for a in A:
        if a not in S:
            ans=S+a
            break
else:
    rs=S[::-1]
    i=1
    while i<26:
        srt=sorted(rs[:i+1])
        if srt[-1]!=rs[i]:
            ans=rs[i+1:][::-1]+srt[srt.index(rs[i])+1]
            break
        i+=1

print(ans)