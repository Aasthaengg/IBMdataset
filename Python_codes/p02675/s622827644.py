N = input("")

h = ["2", "4", "5", "7", "9"]
p = ["0", "1", "6", "8"]

if N[-1] in h:
    print("hon")
elif N[-1] in p:
    print("pon")
else:
    print("bon")