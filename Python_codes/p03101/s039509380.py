a = [list(map(int, input().split())) for i in range(2)]
H = a[0][0] 
W = a[0][1] 
h = a[1][0] 
w = a[1][1] 
my_result = H * W - h * W - H * w + h * w
print(my_result)