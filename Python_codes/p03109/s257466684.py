S = input()

y = S[0:4]
m = S[5:7]
d = S[8:10]

if y < "2019":
    print("Heisei")

elif (y == "2019") and (m < "04"):
    print("Heisei")

elif (y == "2019") and (m == "04") and (d <= "30"):
    print("Heisei")

elif (y == "2019") and (m == "04") and (d > "30"):
    print("TBD")

elif (y == "2019") and (m >= "05"):
    print("TBD")

elif (y > "2019"):
    print("TBD")