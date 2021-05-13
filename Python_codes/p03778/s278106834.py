w,a,b=map(int,input().split())
minu=min(a,b)
maxi=max(a,b)
print(maxi-(minu+w) if maxi-(minu+w)>0 else 0)