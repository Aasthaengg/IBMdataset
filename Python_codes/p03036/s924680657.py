A , B , C = (map(int , input().split()))
a = (A*(C+(0*B))-B)
for i in range(10):
    print(a)
    a = ((A*a)-B)