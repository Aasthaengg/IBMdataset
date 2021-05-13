n = int(input())
a = int(input())
b = int(input())
print(n - a - ((n - a) // b) * b) #(n - a) % b 