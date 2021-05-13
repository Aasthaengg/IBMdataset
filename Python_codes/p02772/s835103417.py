n = int(input())
a = map(int, input().split(" "))

a = [i for i in a if i%2==0]
a2 = [i for i in a if i%3==0 or i%5==0]

print("APPROVED" if a==a2 else "DENIED")