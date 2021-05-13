g,r,a,b=map(int,input().split())
l=["".join(["0" if (retu<a and gyou<b)or(retu>=a and gyou>=b) else "1" for retu in range(r)])for gyou in range(g)]
print(*l,sep="\n")