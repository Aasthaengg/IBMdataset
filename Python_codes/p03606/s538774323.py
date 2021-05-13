n = int(input())
customer = 0;
for i in range(n):
    l,r = map(int, input().split())
    customer += (r - l + 1)

print(customer)
