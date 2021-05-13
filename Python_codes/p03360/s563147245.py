a,b,c = map(int,input().split())
k = int(input())
for i in range(k):
    if(a >= b and a >= c): a *= 2
    elif (b >= a and b >= c): b *= 2
    elif (c >= a and c >= b): c *= 2
print(a + b + c)