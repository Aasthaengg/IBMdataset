S = list(input()) #１文字ずつ
N = len(S)
al=[chr(ord('a') + i) for i in range(26)]
# print('al:',al)
 
flag=0
if S[0]!='A':
    #print('A')
    flag=1
 
else:
    count=0
    for i in range(2,N-1):
        if S[i]=='C':
            count+=1
 
    # print('count:',count)
    if count==1:
        for i in range(N):
            if S[i]!='A' and S[i]!='C':
                if S[i] not in al:
                    flag=1
 
    else:
        flag=1
 
if flag==0:
    print('AC')
else:
    print('WA')