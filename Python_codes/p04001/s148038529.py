S = input()

ans=0
for i in range(1<<(len(S)-1)):
    num = int(S[0])
    cur=0
    for j in range(len(S)-1):
        if i & (1<<j):
            cur+=num
            num=0
        num=num*10+int(S[j+1])
    cur += num
    ans+=cur
print(ans)