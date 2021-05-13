n = int(input())
a,b = map(int,input().split())
min_b = b
min_b_a = a
for i in range(n-1):
    a,b = map(int,input().split())
    if min_b>b:
        min_b = b
        min_b_a = a
print(min_b_a+min_b)