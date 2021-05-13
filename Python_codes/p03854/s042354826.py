S=input()
S=S[::-1]
N=len(S)

index=0
words=["dream","dreamer","erase","eraser"]
for i in range(4):
    words[i]=words[i][::-1]

while index<N:
    word1=S[index:index+5]
    word2=S[index:index+6]
    word3=S[index:index+7]
    if word1 in words:
        index+=5
    elif word2 in words:
        index+=6
    elif word3 in words:
        index+=7
    else:
        print("NO")
        exit()
print("YES")