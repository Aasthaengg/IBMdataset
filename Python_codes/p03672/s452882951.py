s=input()
S=''.join(list(reversed(s)))
a=1
for i in range(len(S)):
    if (len(S)-a)%2==0:
        if S[a:(len(S)+a)//2]==S[(len(S)+a)//2:len(S)]:
            break
        else:
            a+=1
    else:
        a+=1
print(len(S)-a)