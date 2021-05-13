T = input()

status = True
while status:
    if "P?" in T:
        T = T.replace("P?","PD")
    else:
        status = False

status3 = True
while status3:
    if "?D" in T:
        T = T.replace("?D","PD")
    else:
        status3 = False

status2 = True
while status2:
    if "D?" in T:
        T = T.replace("D?","DD")
    else:
        status2 = False

status4 = True
while status4:
    if "?" in T:
        T = T.replace("?","D")
    else:
        status4 = False

print(T)
