liste =[x for x in input()]
def pp():
    for loop in range(3):
        if liste.count(liste[loop]) != 2:
            return "No"
    return "Yes"
print(pp())
