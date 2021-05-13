n=int(input())
a=list(map(int,input().split()))

xor=0#０ならOK -> 実際計算するときれいに0になる

for i in range(n):
    xor=xor^a[i]
if xor==0:
    print("Yes")
else:
    print("No")
