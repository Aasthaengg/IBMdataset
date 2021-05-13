n=int(input())
if n%10==9 or (n-n%10)%100==90:
    print("Yes")
else:
    print("No")
