bef = str(input())
aft = str(input())


print(("No","Yes")[len(aft[0:len(bef)].replace(bef,"") + aft[len(bef):]) == 1])