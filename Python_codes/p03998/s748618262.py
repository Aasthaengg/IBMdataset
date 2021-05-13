a = input()
b = input()
c = input()
a_cnt = 0
b_cnt = 0
c_cnt = 0
next_player = "a"
while True:
    if next_player == "a":
        if a_cnt == len(a):
            print("A")
            exit()
        next_player = a[a_cnt]
        a_cnt += 1
    elif next_player == "b":
        if b_cnt == len(b):
            print("B")
            exit()
        next_player = b[b_cnt]
        b_cnt += 1
    else:
        if c_cnt == len(c):
            print("C")
            exit()
        next_player = c[c_cnt]
        c_cnt += 1
