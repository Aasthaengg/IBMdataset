n = int(input())
a = input()
b = input()
c = input()

answer = 0

for i in range(n):
    int_w = len(set([a[i], b[i], c[i]]))

    if int_w == 3:
        answer += 2
    elif int_w == 2:
        answer += 1
    else:
        pass


print(answer)
