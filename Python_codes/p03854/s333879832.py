S = input()
N = len(S)
i = 0
while N-i >4:
    if S[N-i-5:N-i] == "dream":
        i+=5
    elif N-i>6 and S[N-i-7:N-i]=="dreamer":
        i+=7
    elif S[N-i-5:N-i] == "erase":
        i += 5
    elif N-i>5 and S[N-i-6:N-i] =="eraser":
        i+=6
    else:
        break

if N == i:
    print("YES")
else:
    print("NO")