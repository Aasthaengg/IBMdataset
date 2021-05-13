N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=list(input())
ans=0
dic={'r':'p','s':'r','p':'s'}
score={'r':R,'s':S,'p':P}
past=[]
for i in range(len(T)):
    if i>=K:
        if dic[T[i]]==past[i-K]:
            past.append('0')
            continue
        else:
            ans+=score[dic[T[i]]]
            past.append(dic[T[i]])
    else:
        ans+=score[dic[T[i]]]
        past.append(dic[T[i]])
print(ans)