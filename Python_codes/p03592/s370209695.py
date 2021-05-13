n,m,k=map(int,input().split())

#同じ行、列で2回押すのはノーカウントにできる
#行、列で押した回数を独立にできる
#nのうちp、mのうちq押す
#p*m+q*n-p*q
cnt=0
for p in range(n+1):
    for q in range(m+1):
        if p*m+q*n-2*p*q==k:
            cnt+=1
if cnt>0:
    print("Yes")
else:
    print("No")