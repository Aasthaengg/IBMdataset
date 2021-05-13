x,a,b = (int(T) for T in input().split())
print(['A','B'][min(abs(x-a),abs(x-b))==abs(x-b)])