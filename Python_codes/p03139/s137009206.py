n,a,b=map(int, input().split())
p = min(a,b)
q = max(a+b-n,0)
print(str(p) + " " + str(q))