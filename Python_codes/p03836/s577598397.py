a,b,x,y=map(int,input().split())
ans="UD"[b>y]*abs(b-y)+"LR"[a<x]*abs(a-x)
ans+="UD"[b<y]*abs(b-y)+"LR"[a>x]*abs(a-x)
ans+="LR"[a>x]+"UD"[b>y]*(abs(b-y)+1)+"LR"[a<x]*(abs(a-x)+1)+"UD"[b<y]
ans+="LR"[a<x]+"UD"[b<y]*(abs(b-y)+1)+"LR"[a>x]*(abs(a-x)+1)+"UD"[b>y]
print(ans)