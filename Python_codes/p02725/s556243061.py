n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=[l[i+1]-l[i] for i in range(0,m-1)]
ans.append(n-l[m-1]+l[0])
ans.sort()
print(sum(ans[:m-1]))