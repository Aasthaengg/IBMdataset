a,b,c,k = list(map(int,input().split()))	
x = 10 **18
result = a - b
if result > x:
    print("Unfair")
elif k % 2 == 0:
    print(result)
elif k % 2 == 1:
    result = result * -1
    print(result)
