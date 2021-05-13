# もし全部が9なら、9*N
# 一桁目が9以外なら (一桁目-1) + (len(N)-1 * 9)
# 一桁目が9なら　一桁目が8 + len(N)-1 * 9
S = (input())

if S.count("9") == len(S):
    print(len(S)*9)

elif len(S) == 1:
    print(int(S))

elif S.count("9") == (len(S)-1) and (S[0]!="9"):
    print((int(S[0])) + (len(S)-1)*9)

elif S[0] == "9":
    print(8 + ((len(S)-1)*9))
else:
    print((int(S[0])-1) + (len(S)-1)*9)