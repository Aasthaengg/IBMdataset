n = int(input())
max_a = 0
st_b = 0
for i in range(n):
    a,b = map(int,input().split())
    if max_a < a:
        max_a = a
        st_b = b
print(max_a+st_b)