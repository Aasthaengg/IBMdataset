def compare(a, b):
    if a < b :
        return "<"
    elif a > b :
        return ">"
    else:
        return "=="

(a, b) = input().split(" ")
print("a " + compare(int(a), int(b)) + " b")