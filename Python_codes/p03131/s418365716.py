k, a, b = map(int, input().split())
if 2 >= b-a  or a >= k:
    print(k+1)

else:
    print(b + ((k-a+1)//2-1)*(b-a) + ((k-a+1)%2))