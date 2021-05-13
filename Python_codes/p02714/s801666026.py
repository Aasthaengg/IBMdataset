#D
N = int(input())
S = input()

ans = S.count('R')*S.count('G')*S.count('B')

for start in range(0,N-2):
    for interval in range(1,N):
        try:
            if S[start] != S[start+interval] and S[start] != S[start+2*interval] and S[start+interval] != S[start+2*interval]:
                ans -= 1
        except IndexError:
            break
print(ans)