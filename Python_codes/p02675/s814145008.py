n = input()

remainder = int(n[-1])
if remainder in (2, 4, 5, 7, 9): print("hon")
elif remainder in (0,1,6,8): print("pon")
elif remainder is 3: print("bon")