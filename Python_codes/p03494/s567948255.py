n=int(input())
val1 = input().split(" ")
val2=[int(i) for i in val1]

w = 0

while True:
    v = 0
    for i in range(n):
        if val2[i] % 2 == 1:
            v = 1
    if v ==1:
        break
    if v ==0:
        for i in range(n):
            val2[i] = val2[i]/2
        w += 1

print(w)