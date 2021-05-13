N=int(input())
odd=False
for i in range(N):
    a=int(input())
    if a%2==1:
        odd=True

if odd:
    print("first")
else:
    print("second")

