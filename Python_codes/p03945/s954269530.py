S=input()
if len(S)==max(S.count('W'),S.count('B')):
    print(0)
    exit()
else:
    t=''
    cnt=0
    for i in S:
        if i!=t:
            cnt+=1
            t=i

    print(cnt-1)