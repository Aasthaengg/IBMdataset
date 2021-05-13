#ABC122-D We Like AGC
"""
条件を満たす文字列は、
xをACGTのいずれかとして
AGC
GAC
ACG
AxGC
AGxC
のいずれも文字列内に無い状態のことを言う。
上の条件から、末尾に文字を付け足そうとした時に、それに関与する文字列は
末尾3文字のみであり、それより前の状態は関係ない。
つまり、前3文字の結果を保存し続ければ3**4のdpテーブルを用いて求めることができる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7

n = int(readline())

dic1 = {"A":0,"G":1,"C":2,"T":3}

#dp[i][j][k][l]:i文字目に3文字前がjで2文字前がkで1文字前がlである時のそこまでにあり得る通り数
#j,k,lにおいて、A,G,C,T=0,1,2,3と対応させる
dp = [[[[0]*4 for b in range(4)] for a in range(4)]for _ in range(n+1)]
dp[0][3][3][3] = 1

for i in range(n):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0:
                    continue
                for m in range(4):
                    if k == dic1["A"] and l == dic1["G"] and m == dic1["C"]: #AGC
                        continue
                    if k == dic1["G"] and l == dic1["A"] and m == dic1["C"]: #GAC
                        continue
                    if k == dic1["A"] and l == dic1["C"] and m == dic1["G"]: #ACG
                        continue
                    if j == dic1["A"] and l == dic1["G"] and m == dic1["C"]: #AxGC
                        continue
                    if j == dic1["A"] and k == dic1["G"] and m == dic1["C"]: #AGxC
                        continue
                    
                    dp[i+1][k][l][m] += dp[i][j][k][l] #次の状態に今を足す
                    dp[i+1][k][l][m] %= mod
                    


ans = 0
i = n
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[i][j][k][l]

print(ans%mod)
