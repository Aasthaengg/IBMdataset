def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        for j in range(1,len(S)-i+1):
            # 数値S[i]を下からj桁目の数として受け取るパターン数は
            # (1) (残りのSの長さ-1)個の場所に'+'をいれるパターン数 S[:i]
            # (2) (残りのSの長さ-1)個の場所に'+'をいれるパターン数 S[i:]
            # の積に他ならない
            ans += int(S[i])*(10**(j-1)) * (2**i) * (2**max(0,(len(S)-i-j-1)))
    print(ans)
main()
