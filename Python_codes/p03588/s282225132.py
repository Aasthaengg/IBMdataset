n = int(input())
li_input = list()
for i in range(n):
    li_input.append(list(map(int, input().split())))

li_s = sorted(li_input, key=lambda x: x[0])

print((li_s[-1][0]) + (li_s[-1][1]))
