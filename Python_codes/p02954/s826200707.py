"""
1.連続するRを探す(rf-re)
2.連続するLを探す(lf-le)
3.rf-leの間で偶奇をカウント、re、lfにその数を代入
"""

S = input()+"R"
N = len(S)
Rli = [0]*(N-1)

rf=re=lf=le=-1
rf = 0

for i in range(N):
  if re == -1:
    #R search
    if S[i] == "L":
      re = i-1
      lf = i
  else:
    #L search
    if S[i] == "R":
      le = i-1
      bet = le-rf+1
      if bet%2 == 0:
        Rli[re] = Rli[lf] = bet//2
      else:
        if rf%2 == 0:
          ki = (bet-1)//2
        else:
          ki = (bet+1)//2
        if re%2 == 0:
          Rli[re] = bet-ki
          Rli[lf] = ki
        else:
          Rli[re] = ki
          Rli[lf] = bet-ki
      rf=re=lf=le=-1
      rf = i
      
print(" ".join(map(str,Rli)))