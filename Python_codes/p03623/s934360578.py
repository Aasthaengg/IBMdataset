x,a,b=map(int,input().split())
ans={abs(x-a):'A',abs(x-b):'B'}
print(ans[min(abs(x-a),abs(x-b))])