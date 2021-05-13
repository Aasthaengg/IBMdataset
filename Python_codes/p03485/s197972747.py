a,b = input().split(" ")
a,b = int(a),int(b)
ab = a + b
if ab % 2 != 0:
    print(int((a+b+1)/2))
else:
    print(int((a+b)/2))