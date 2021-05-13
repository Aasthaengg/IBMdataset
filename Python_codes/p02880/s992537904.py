num = int(input())
if num in [i*j for i in range(1,10) for j in range(1,10)]:
    print("Yes")
else:
    print("No")