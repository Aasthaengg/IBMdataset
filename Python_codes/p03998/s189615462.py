ABC = "ABC"
s = [input()+ABC[i] for i in range(3)]
turn = s[0]
card = 0
count = [1, 0, 0]

for i in range(305):
    if turn[card] == "a":
        turn = s[0]
        card = count[0]
        count[0] += 1
    elif turn[card] == "b":
        turn = s[1]
        card = count[1]
        count[1] += 1
    else:
        turn = s[2]
        card = count[2]
        count[2] += 1
    
    if turn[card] == "A":
        print("A")
        exit()
    if turn[card] == "B":
        print("B")
        exit()
    if turn[card] == "C":
        print("C")
        exit()