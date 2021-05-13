a,b,k = map(int,input().split())

a,b = max(a-k,0), max(min(b-(k-a),b),0)

print(a,b)