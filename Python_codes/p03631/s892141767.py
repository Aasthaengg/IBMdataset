def resolve():
    n = input()
    check = ""
    true_check = ""
    for i in range(len(n)):
        true_check += "T"
        if n[i] == n[len(n)-i-1]:
            check += "T"
        else:
            check += "F"
            print("No")
            break
    if not("F" in check) and check == true_check:
        print("Yes")
resolve()