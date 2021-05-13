S = input()
T = input()

flag = False
count = 0
while True:
    if S == T:
        flag = True
        break

    if count == len(S):
        break
    
    S = S[-1] + S[:len(S) - 1]
    count += 1

if flag:
    print("Yes")
else:
    print("No")