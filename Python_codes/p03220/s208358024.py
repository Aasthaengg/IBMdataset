N = int(input())
MM = input().split()
T = int(MM[0])
A = int(MM[1])
LL = input().split()
jisyo ={}
for i in range(N):
  H = float(T) - float(LL[i])*0.006
  PPP =  A - H
  jisyo[abs(PPP)] = i+1
dic2 = sorted(jisyo.items())
print(dic2[0][1])