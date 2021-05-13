s = int(input())

prev = []
count = 1
while(s not in prev):
    prev.append(s)
    if(s % 2 == 0):
        s = s/2
    else:
        s = 3*s + 1
    count += 1
print(count)
