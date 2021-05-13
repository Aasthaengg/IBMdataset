N,K=list(map(int,input().split()))
S = list(input())

for i in range(len(S)):
    if i != K-1:
        print(S[i],end='')
    else:
        print(chr(ord(S[i])+32),end="")
