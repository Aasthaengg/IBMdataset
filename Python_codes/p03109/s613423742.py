Y, M, D = map(int, input().split("/"))

if M <= 4:
    if D <= 30:
        print("Heisei")
    else:
        print("TBD")
else:
    print("TBD")
