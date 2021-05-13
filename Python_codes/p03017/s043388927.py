#ランレングス圧縮
def rle_comp(S):
    rle = []
    pre = 'X'
    chain = 1
    for c in S:
        if c == pre:
            chain += 1
        else:
            if pre != 'X':
                rle.append([pre,chain])
            
            pre = c
            chain = 1
    rle.append([pre,chain])

    #print(rle)
    return rle

N,A,B,C,D = map(int,input().split())
S = input()
#S = S[:A-1] + 'A' + S[A:]
#S = S[:B-1] + 'B' + S[B:]
#print(S)
ans = "Yes"
#すぬけ君がふぬけ君を2マスジャンプで追い越しが不要な場合
if C < D:
    rle = rle_comp(S[A-1:D])
    for i in range(len(rle)):
        #2マスジャンプで岩をやりすごせるか判定
        if rle[i][0] == '#' and rle[i][1] >= 2:
            ans = "No"
#すぬけ君がふぬけ君を2マスジャンプで追い越しが必要な場合
else:
    rle = rle_comp(S[A-1:C])
    for i in range(len(rle)):
        #2マスジャンプで岩をやりすごせるか判定
        if rle[i][0] == '#' and rle[i][1] >= 2:
            ans = "No"

    space = False
    #ふぬけ君がスタート地点またはゴール地点にいる状態で追い越しをする場合を考慮するため
    #範囲を1つずつ広げる
    rle = rle_comp(S[B-2:D+1])
    for i in range(len(rle)):
        #追い越しができるか判定
        if rle[i][0] == '.' and rle[i][1] >= 3:
            space = True
    
    if space == False:
        ans = "No"

print(ans)