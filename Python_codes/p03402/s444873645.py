A,B=map(int,input().split())
UP=[["#"]*100 for _ in range(50)]
DN=[["."]*100 for _ in range(50)]
i,j=0,0
a=1
# 偶数行目の偶数番目を白く塗る
while a<A:
    UP[j][i]="."
    a+=1
    i+=2
    if i>=100:
        j+=2
        i=0
i,j=0,1
b=1
# 奇数行目の偶数番目を黒く塗る
while b<B:
    DN[j][i]="#"
    b+=1
    i+=2
    if i>=100:
        j+=2
        i=0
print("{} {}".format(100, 100))
print("\n".join("".join(i) for i in UP))
print("\n".join("".join(i) for i in DN))