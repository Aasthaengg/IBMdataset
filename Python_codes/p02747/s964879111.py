S = input()
l = len(S)


judge=True
if l%2==0:
    for i in range(l//2):
        if not S[2*i:2*(i+1)]=="hi":
            judge=False
    if judge:
        print("Yes")
    else:
        print("No")
else:
    print("No")
