grade = []
while True:
    [m, f, r] = map(int, input().split())
    if (m==-1)and(f==-1)and(r==-1):
        break
    else:
        score = m + f
        if (m==-1)or(f==-1):
            grade.append("F")
        elif score>=80:
            grade.append("A")
        elif 65<=score<80:
            grade.append("B")
        elif 50<=score<65:
            grade.append("C")
        elif 30<=score<50:
            if r>=50:
                grade.append("C")
            else:
                grade.append("D")
        else:
            grade.append("F")

for i in grade:
    print(i)