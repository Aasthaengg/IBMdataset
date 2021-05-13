def compare(a, b, c):
    if a >= b :
        return "No"
    if b >= c :
        return "No"
    return "Yes"

(a, b, c) = input().split(" ")
print(compare(int(a), int(b), int(c)))