n=int(input())
*a,=map(int,input().split())

b=sorted([(a[i],str(i+1)) for i in range(n)],key=lambda x:x[0])

print(' '.join([c for _,c in b]))
