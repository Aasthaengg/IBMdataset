def mult(n):
    res = 0 
    for i in n:
        res += int(i)

    if res%9 != 0:
        return "No"
    return "Yes"

n = input()
print(mult(n))