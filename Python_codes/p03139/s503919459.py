N,A,B = map(int,input().split())

mx = min(A,B)
mi = max(A+B-N,0)

print(str(mx) + " " + str(mi))
