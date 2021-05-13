x = list(input())
sta = 0
pop = 0
for i in range(len(x)):
    if x[i] == 'S':
        sta += 1
    elif sta > 0:
        sta -= 1
        pop += 1
print(len(x)-2*pop)