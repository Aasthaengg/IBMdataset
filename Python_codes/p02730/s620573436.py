S=str(input())
N=len(S)
if S!=S[::-1]:#Sと反転したSが不一致
    print('No')
else:
    S1=S[0:(N-1)//2]#Sが1文字目～(N-1)/2番目の場合
    S2=S[(N+1)//2:N]#Sが(N+3)/2～N番目の場合
    if S1==S1[::-1] and S2==S2[::-1]:
        print('Yes')
    else:
        print('No')