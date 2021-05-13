S=input()
T=input()
#条件は、SとTで、同じ文字が同じ場所に同数存在していること
d={}
#used=set()
for (s,t) in zip(S,T):
    try:
        if d[s]!=t:
            print("No")
            exit()
    except KeyError:
        #sとtの対応関係を記録
        d[s]=t

v=d.values() 
if len(v)!=len(set(v)):
    print("No")
else:
    print("Yes")