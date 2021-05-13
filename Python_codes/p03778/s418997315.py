#056_B
w,a,b=map(int,input().split())
print(0 if abs(b-a)<=w else min(abs(b-w-a),abs(b+w-a)))