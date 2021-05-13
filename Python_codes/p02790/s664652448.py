a,b=map(int,input().split())
new_a=str(a)*b
new_b=str(b)*a
if new_a < new_b:
    print(new_a)
else:
    print(new_b)