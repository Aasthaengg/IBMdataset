X=int(input())
if X>3000:
    print(1)
elif X<100:
    print(0)
else:
    i=1
    while i<=X:
        if 100*i<=X and 105*i>=X:
            print(1)
            quit()
        i+=1
    print(0)