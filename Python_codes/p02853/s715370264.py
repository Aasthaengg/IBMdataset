X , Y = map(int,input().split())

if X == 1 and Y == 1:
    print("1000000")

elif X == 1 and Y == 2:
    print("500000")

elif X == 1 and Y == 3:
    print("400000")

elif X == 2 and Y == 3:
    print("300000")

elif X == 2 and Y == 2:
    print("400000")
   
elif X == 3 and Y == 3:
    print("200000")

elif X == 3 and Y == 2:
    print("300000")
    
elif X == 2 and Y == 1:
    print("500000")

elif X == 3 and Y == 1:
    print("400000")

elif X == 1 and Y >= 4:
    print("300000")

elif X == 2 and Y >= 4:
    print("200000")  

elif X == 3 and Y >= 4:
    print("100000")

elif X >= 4 and Y == 1:
    print("300000")

elif X >= 4 and Y == 2:
    print("200000")

elif X >= 4 and Y == 3:
    print("100000")

else:
    print("0")
