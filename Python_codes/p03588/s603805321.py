N=int(input())
a=0#Aの最大値
b=0
for i in range(N):
    A,B=map(int,input().split())
    if a<A:
        a=A
        b=A+B#aが最大値の時だけA+Bを更新する
print(b)