from fractions import gcd
n = int(input())
a_input = list(map(int,input().split()))

x = a_input.pop(0)
for i in range(len(a_input)):
    x = gcd(x,a_input[i])
print(x)