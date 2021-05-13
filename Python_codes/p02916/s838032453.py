num = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))
val = 0
 
for i in range(num):
    val += y[x[i]-1]
    if 1<=i and x[i]-x[i-1] == 1:
        val += z[x[i]-2]
 
print(val)