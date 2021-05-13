time_input = input()
time = time_input.split()

A = int(time[0])
B = int(time[1])

if A + B >= 24:
    print(A + B - 24)

else:
    print(A + B)