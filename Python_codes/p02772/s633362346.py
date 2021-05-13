f = "APPROVED"
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if not (i&1) and i%3!=0 and i%5!=0:
        f = "DENIED"
print(f)