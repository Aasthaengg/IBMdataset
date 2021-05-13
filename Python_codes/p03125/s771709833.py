a,b=map(int,input().split())
print((str(b-a),str(a+b))[b%a==0])