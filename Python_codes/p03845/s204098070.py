s = input()
n = int(s)

questions = []
copy = []
answer = 0

x = input().split()

for num in range(len(x)):
    questions.append(x[num])
    copy.append(x[num])

v = input()
m = int(v)

for num in range(m):
    d = input().split()
    questions[int(d[0]) - 1] = int(d[1])
    for y in range(len(questions)):
        answer += int(questions[y])
    print(answer)
    answer = 0
    for z in range(len(questions)):
        questions[z] = copy[z]
    





    
