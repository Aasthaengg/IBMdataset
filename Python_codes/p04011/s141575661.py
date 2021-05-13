#宿泊数N,金額を表す計算用宿泊日数K,K泊目の金額X,K+1泊目の金額
N=int(input())
K=int(input())
X=int(input())
Y=int(input())

if N<K:
    a=N*X
    b=0
else:
    a=K*X
    b=(N - K) * Y

print(a+b)