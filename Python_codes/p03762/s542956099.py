n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
mod = 1000000007

keisu = len(x)-1
keisu_kaisa = keisu
ans = 0
for i in range(1,n):
  #print(keisu)
  ans = ans + 1*(x[i]-x[i-1])*keisu
  keisu_kaisa = keisu_kaisa -2
  keisu = keisu +(keisu_kaisa)
  ans = ans % mod
  
keisu = len(y)-1
keisu_kaisa = keisu
ans_2 = 0
for i in range(1,m):
  ans_2 = ans_2 + ans*(y[i]-y[i-1])*keisu
  keisu_kaisa = keisu_kaisa -2
  keisu = keisu +(keisu_kaisa)
  ans_2 = ans_2 % mod  
print(ans_2)
