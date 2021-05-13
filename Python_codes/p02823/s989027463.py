n,a,b = map(int,input().split())
if abs(a-b)%2:
    print(abs(a-b)//2+1+min((abs(1-a),abs(n-a),abs(1-b),abs(n-b))))
else:
    print(abs(a-b)//2)
