def eval(a, b, c):
    if a < b and b < c:
        print ("Yes")
    else:
        print ("No")
  

a = list(map(int, input().split()))

eval(a[0], a[1], a[2])