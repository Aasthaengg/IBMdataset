n=input().split()
A=int(n[0])
B=int(n[1])

if 13<=A:
    print(B)
elif 6<=A<=12:
    print(int(B/2))
elif A<=5:
    print("0")