# AOJ ITP1_7_A

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    while True:
        data = numinput()
        if data[0] < 0 and data[1] < 0 and data[2] < 0: break
        grade = ""
        if data[0] + data[1] >= 80: grade = "A"
        elif data[0] + data[1] >= 65: grade = "B"
        elif data[0] + data[1] >= 50: grade = "C"
        elif data[0] + data[1] >= 30:
            if data[2] >= 50: grade = "C"
            else: grade = "D"
        else:
            grade = "F"
        if data[0] < 0 or data[1] < 0: grade = "F"
        print(grade)

if __name__ == "__main__":
    main()

