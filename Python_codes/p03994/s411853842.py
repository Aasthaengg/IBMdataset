S = list(input())
L = len(S)
K = int(input())
idx = 0
while K > 0:
    # aまでの必要な回数
    if S[idx] == "a" and idx < L-1:
        idx += 1
        continue
        
    k = 123 - ord(S[idx])
    if k > K:
        if idx < L-1:
            # aまで操作できないのに、操作すると辞書順でより後ろの文字列になってしまうので、次の文字へ
            idx += 1
        else:
            # 一番後ろの場合
            t = chr(ord(S[idx])+(K%26))
            S[idx] = t
            K = 0
    else:
        K -= k
        S[idx] = "a"
        if idx < L-1:
            idx += 1

print("".join(S))
