a,b,c = map(int, input().split())

a_b = a+b
a_c = a+c
b_c = b+c

print(min(a_b,a_c,b_c))